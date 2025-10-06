отвечаю «пошагово», для твоих связок. Везде цель — минимум конфликтов и предсказуемая история.

⸻

Преднастройка (один раз)

git remote add upstream https://github.com/FreeCAD/FreeCAD.git   # если ещё нет
git fetch --all

# удобнее держать «зеркала» апстрима по сериям

git checkout -B mirror/A  upstream/`<branch-or-tag-for-A>`   # напр. releases/FreeCAD-0-21
git checkout -B mirror/B  upstream/`<branch-or-tag-for-B>`   # напр. upstream/main или 0-22

# включить «автопамять» конфликтов и удобный вид

git config --global rerere.enabled true
git config --global rerere.autoupdate true
git config --global merge.conflictStyle zdiff3

Правило: mirror/* — всегда точные копии апстрима (только reset --hard, никакого merge).

⸻

1) upstream_A → integration_A  (обновляем integration ветку от апстрима)

Кейс 1: integration_A = mirror/A + ваши несколько коммитов сверху
→ просто rebase на свежий апстрим:

git fetch upstream
git checkout mirror/A
git reset --hard upstream/`<A>`
git push -f origin mirror/A

git checkout integration/A
git rebase mirror/A -X theirs    # предпочесть изменения апстрима при коллизиях

# если конфликты: правим → git add → git rebase --continue

git push origin integration/A --force-with-lease

Кейс 2: в integration_A были merge-коммиты
→ сохраните их структурно:

git checkout integration/A
git rebase --rebase-merges mirror/A -X theirs
git push --force-with-lease

Кейс 3: integration_A накопил «мусор» (много старых мержей)
→ превратить в тонкий слой поверх апстрима:

# найдём старую базу

BASE=$(git merge-base integration/A mirror/A)

# перепишем только наши коммиты поверх новой базы

git rebase --onto mirror/main $BASE integration/main -X theirs
git push --force-with-lease

Почему rebase, а не merge? — ребейз делает вид, что ваши коммиты написаны «после» апстрима; зона конфликтов сильно меньше.

⸻

2) integration_A → feature_B и обратно

Старт фичи от integration_A

git checkout -b feature/B integration/A

# работа → коммиты

Подтягиваем апстримные изменения в фичу (без обратных merge-петель):

git fetch origin
git checkout feature/B
git rebase origin/integration/A -X theirs

# правим конфликты → add → rebase --continue

git push --force-with-lease

Возврат фичи в integration_A
Рекомендация — через PR, «fast-forward» или «squash», чтобы не тащить техдолг:

# локально (если без PR):

git checkout integration/A
git merge --ff-only feature/B    # или: git merge --squash feature/B && git commit
git push

    •	--ff-only исключает лишние merge-коммиты.
	•	Если фича большая — --squash сведёт её к одному «интеграционному» коммиту.

⸻

3) integration_B → feature_B и обратно

(«Переезд» фичи на новую интеграционную базу)

Когда A → B (напр., с 0.21 на 0.22), надо переставить основание ветки:

git fetch origin
git checkout feature/B

# найдём старую базу фичи на A:

OLD_BASE=$(git merge-base feature/B origin/integration/A)

# перенесём фичу на новую базу B:

git rebase --onto origin/integration/B $OLD_BASE feature/B -X theirs

# тесты…

git push --force-with-lease

Возврат в integration/B — как в пункте 2 (PR, ff-only/squash).

⸻

4) integration_A → release_A  (заморозка релиза)

Вариант «чистый срез» (релиз = текущее состояние integration):

git checkout -b release/A integration/A
git push -u origin release/A
git tag -a engine-A.0 -m "Engine A.0 (based on FreeCAD A @ `<shortsha>`)"
git push origin engine-A.0

Вариант «выборочные фичи» (не всё из integration попадает в релиз):

git checkout -b release/A mirror/A     # база = чистый апстрим A
git cherry-pick <коммиты из feature/*, integration/A>  # только нужное
git push -u origin release/A
git tag -a engine-A.0 -m "…"
git push origin engine-A.0

Релизы всегда помечай тегами. Явно указывай базу апстрима в сообщении тега или в имени, напр.:
engine-0.21.3+fc-0.21.2.

⸻

5) release_A → hotfix

(точечные фиксы, минимум конфликтов, с обратной «переноской»)

Готовим хотфикс и выпускаем патч:

git checkout -b hotfix/A-fix-123 release/A

# правки → коммиты

git checkout release/A
git merge --ff-only hotfix/A-fix-123
git tag -a engine-A.1 -m "Hotfix #123: …"
git push origin release/A engine-A.1

Форвард-порт хотфикса (чтобы не потерялся в новых ветках):

# та же правка должна попасть в integration/A и, возможно, в integration/B

git checkout integration/A
git cherry-pick -x <hash хотфикса из release/A>
git push

git checkout integration/B
git cherry-pick -x <hash хотфикса> || echo "требуется ручная адаптация"
git push

(Сделай в CI проверку: «все хотфиксы из release/A присутствуют в integration/B».)

⸻

Политики, которые резко снижают конфликты
	•	Одностороннее движение баз: фичи только ребейзятся на integration; integration не «тянет назад» код из фич без PR.
	•	Защищённые ветки: mirror/*, integration/*, release/* — защищены; для mirror/* разрешён только force-push после reset --hard upstream.
	•	Авто-синк зеркал: cron/Actions раз в день:

git fetch upstream
for S in A B; do
  git checkout -B mirror/$S upstream/<branch-or-tag-for-$S>
  git push -f origin mirror/$S
done

    •	Авто-ребейз integration: если mirror/A обновился → бот делает
git rebase --rebase-merges mirror/A -X theirs для integration/A.
При конфликте — открывает PR «manual-resolve».
	•	Гигиена фич: маленькие, изолированные коммиты; минимум правок в «горячих» файлах апстрима; по возможности — #ifdef ENGINE_FEATURE/плагины/модули.
	•	.gitattributes для шума: отключи мерж генерируемых/лок-файлов (точечно merge=ours|theirs).

⸻

Быстрые «шпаргалки» по командам

Ребейз фичи на текущую интеграцию

git checkout feature/B
git rebase origin/integration/A -X theirs

Переезд фичи с A на B

OLD_BASE=$(git merge-base feature/B origin/integration/A)
git rebase --onto origin/integration/B $OLD_BASE feature/B -X theirs

Сделать релиз из integration

git checkout -b release/A integration/A
git tag -a engine-A.0 -m "…"
git push origin release/A engine-A.0

Хотфикс релиза + форвард-порт

git checkout -b hotfix/A-xxx release/A

# fix…

git checkout release/A && git merge --ff-only hotfix/A-xxx && git push
git tag -a engine-A.1 -m "…" && git push origin engine-A.1
git checkout integration/A && git cherry-pick -x `<fix>` && git push
git checkout integration/B && git cherry-pick -x `<fix>` && git push

Если хочешь, напишу тебе два готовых GitHub Actions:
	1.	sync mirror/* + auto-rebase integration/*,
	2.	сборка артефактов «по тегу engine-* → GitHub Release».
