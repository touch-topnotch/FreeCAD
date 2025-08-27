'''
Тестовый скрипт для проверки аутентификации на новом сервисе
1. Автологин через keyring
2. Логин через username/password
3. Регистрация нового аккаунта
4. Проверка текущего пользователя
'''

import requests
import keyring
import json

API_BASE_URL = "https://touchtopnotch.com/api/auth"
APP_NAME = "TouchTopnotch_Auth"

def auto_login():
    """Автологин через сохраненные в keyring данные"""
    saved_username = keyring.get_password(APP_NAME, "username")
    saved_password = keyring.get_password(APP_NAME, "password")
    
    if saved_username and saved_password:
        print(f"Пытаемся автологин с пользователем: {saved_username}")
        response = requests.post(f"{API_BASE_URL}/token", 
                               data={"username": saved_username, "password": saved_password})
        
        if response.status_code == 200:
            print("✅ Автологин успешен!")
            return response.json()
        else:
            print(f"❌ Автологин не удался: {response.status_code}")
            print(response.text)
            return None
    else:
        print("❌ Нет сохраненных данных для автологина")
        return None

def login_via_password(username: str, password: str):
    """Логин через username/password"""
    print(f"Пытаемся войти с пользователем: {username}")
    
    response = requests.post(f"{API_BASE_URL}/token", 
                           data={"username": username, "password": password})
    
    if response.status_code == 200:
        print("✅ Логин успешен!")
        # Сохраняем данные в keyring
        keyring.set_password(APP_NAME, "username", username)
        keyring.set_password(APP_NAME, "password", password)
        return response.json()
    else:
        print(f"❌ Логин не удался: {response.status_code}")
        print(response.text)
        return None

def sign_up(username: str, email: str, password: str, full_name: str):
    """Регистрация нового пользователя"""
    print(f"Регистрируем нового пользователя: {username}")
    
    data = {
        "username": username,
        "email": email,
        "password": password,
        "full_name": full_name
    }
    
    response = requests.post(f"{API_BASE_URL}/register", json=data)
    
    if response.status_code == 200:
        print("✅ Регистрация успешна!")
        return response.json()
    else:
        print(f"❌ Регистрация не удалась: {response.status_code}")
        print(response.text)
        return None

def get_current_user(token: str):
    """Получение информации о текущем пользователе"""
    print("Получаем информацию о текущем пользователе...")
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_BASE_URL}/me", headers=headers)
    
    if response.status_code == 200:
        print("✅ Информация о пользователе получена!")
        return response.json()
    else:
        print(f"❌ Не удалось получить информацию: {response.status_code}")
        print(response.text)
        return None

def logout(token: str):
    """Выход из системы"""
    print("Выходим из системы...")
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{API_BASE_URL}/logout", headers=headers)
    
    if response.status_code == 200:
        print("✅ Выход выполнен успешно!")
        # Удаляем сохраненные данные
        keyring.delete_password(APP_NAME, "username")
        keyring.delete_password(APP_NAME, "password")
        return True
    else:
        print(f"❌ Ошибка при выходе: {response.status_code}")
        print(response.text)
        return False

def test_oauth_urls():
    """Тестирование OAuth URL"""
    print("Получаем OAuth URLs...")
    
    # Google OAuth URL
    response = requests.get(f"{API_BASE_URL}/google/url")
    if response.status_code == 200:
        print("✅ Google OAuth URL получен")
        print(f"URL: {response.json().get('url', 'N/A')}")
    else:
        print(f"❌ Ошибка получения Google OAuth URL: {response.status_code}")
    
    # GitHub OAuth URL
    response = requests.get(f"{API_BASE_URL}/github/url")
    if response.status_code == 200:
        print("✅ GitHub OAuth URL получен")
        print(f"URL: {response.json().get('url', 'N/A')}")
    else:
        print(f"❌ Ошибка получения GitHub OAuth URL: {response.status_code}")

async def test_authentication() -> str | None:
    """
    Элегантный метод для получения bearer токена через веб-интерфейс.
    Открывает браузер, ждет авторизации пользователя, возвращает токен.
    """
    import webbrowser
    import time
    import json
    from urllib.parse import urlencode
    
    print("\n🌐 Запуск автоматизированного теста аутентификации")
    print("=" * 60)
    
    # Шаг 1: Открываем сайт авторизации
    auth_url = "https://touchtopnotch.com/auth/"
    print(f"1️⃣ Открываем сайт авторизации: {auth_url}")
    
    try:
        webbrowser.open(auth_url)
        print("✅ Браузер открыт")
    except Exception as e:
        print(f"❌ Ошибка открытия браузера: {e}")
        return None
    
    # Шаг 2: Ждем ввода от пользователя
    print("\n2️⃣ Ожидание авторизации пользователя...")
    print("📝 Пожалуйста, выполните следующие действия:")
    print("   - Зарегистрируйтесь или войдите на сайте")
    print("   - После успешной авторизации нажмите Enter в этом терминале")
    
    try:
        input("\n⏳ Нажмите Enter когда авторизация завершена: ")
    except KeyboardInterrupt:
        print("\n❌ Тест прерван пользователем")
        return None
    
    # Шаг 3: Получение токена через специальный endpoint
    print("\n3️⃣ Получение токена через специальный endpoint...")
    
    # Открываем специальную страницу для извлечения токена
    token_extractor_url = "https://touchtopnotch.com/api/auth/token-extractor"
    print(f"🔗 Открываем страницу извлечения токена: {token_extractor_url}")
    
    try:
        webbrowser.open(token_extractor_url)
        print("✅ Страница извлечения токена открыта")
    except Exception as e:
        print(f"❌ Ошибка открытия страницы: {e}")
        print(f"📋 Откройте вручную: {token_extractor_url}")
    
    print("📋 На странице:")
    print("   - Если токен найден, нажмите 'Копировать токен'")
    print("   - Если токен не найден, вернитесь на сайт авторизации")
    print("   - После копирования токена, вставьте его ниже")
    
    # Шаг 4: Запрашиваем токен у пользователя
    try:
        token = input("\n📝 Вставьте полученный токен: ").strip()
        
        if not token:
            print("❌ Токен не введен")
            return None
        
        # Убираем "Bearer " если пользователь его ввел
        if token.startswith("Bearer "):
            token = token[7:]
        
        # Проверяем токен
        print(f"\n🔍 Проверяем токен: {token[:20]}...")
        user_info = get_current_user(token)
        
        if user_info:
            print("✅ Токен валидный!")
            print(f"👤 Пользователь: {user_info.get('username', 'N/A')}")
            print(f"📧 Email: {user_info.get('email', 'N/A')}")
            print(f"👨‍💼 Полное имя: {user_info.get('full_name', 'N/A')}")
            
            # Сохраняем в keyring для автологина
            username = user_info.get('username')
            if username:
                print(f"\n💾 Сохраняем данные для автологина...")
                keyring.set_password(APP_NAME, "username", username)
                print("✅ Username сохранен в keyring")
            
            return token
        else:
            print("❌ Токен невалидный или истек")
            return None
            
    except KeyboardInterrupt:
        print("\n❌ Тест прерван пользователем")
        return None
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None

def test_web_login():
    """Тестирование логина через веб-интерфейс"""
    print("\n🌐 Тестирование логина через веб-интерфейс")
    print("=" * 60)
    print("1. Откройте https://touchtopnotch.com/auth/ в браузере")
    print("2. Зарегистрируйтесь или войдите через форму")
    print("3. После успешного входа, скопируйте токен из localStorage")
    print("4. Вставьте токен ниже:")
    
    try:
        token = input("\nВставьте Bearer токен (или нажмите Enter для пропуска): ").strip()
        
        if not token:
            print("Токен не введен, пропускаем тест")
            return None
        
        # Убираем "Bearer " если пользователь его ввел
        if token.startswith("Bearer "):
            token = token[7:]
        
        print(f"\n🔍 Проверяем токен: {token[:20]}...")
        
        # Проверяем токен
        user_info = get_current_user(token)
        if user_info:
            print("✅ Токен валидный!")
            print(f"👤 Пользователь: {user_info.get('username', 'N/A')}")
            print(f"📧 Email: {user_info.get('email', 'N/A')}")
            print(f"👨‍💼 Полное имя: {user_info.get('full_name', 'N/A')}")
            
            # Сохраняем в keyring для автологина
            username = user_info.get('username')
            if username:
                print(f"\n💾 Сохраняем данные для автологина...")
                # Пароль мы не знаем, но можем сохранить username
                keyring.set_password(APP_NAME, "username", username)
                print("✅ Username сохранен в keyring")
            
            return token
        else:
            print("❌ Токен невалидный или истек")
            return None
            
    except KeyboardInterrupt:
        print("\n❌ Тест прерван пользователем")
        return None
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None

def get_token_from_localstorage_guide():
    """Инструкция по получению токена из localStorage"""
    print("\n📖 Как получить токен из браузера:")
    print("1. Откройте https://touchtopnotch.com/auth/")
    print("2. Войдите в систему")
    print("3. Откройте Developer Tools (F12)")
    print("4. Перейдите во вкладку Console")
    print("5. Выполните команду: localStorage.getItem('access_token')")
    print("6. Скопируйте полученный токен")
    print("7. Вставьте его в тест выше")

async def main():
    print("🧪 Тестирование аутентификационного сервиса")
    print("=" * 50)
    
    # Тест 1: Автоматизированная аутентификация через веб-интерфейс
    print("\n1️⃣ Тест автоматизированной аутентификации:")
    token = await test_authentication()
    
    if token:
        access_token = token
        print(f"\n🎉 Успешно получили токен через веб-интерфейс!")
        
        # Тест 2: Получение информации о пользователе
        print("\n2️⃣ Тест получения информации о пользователе:")
        user_info = get_current_user(access_token)
        if user_info:
            print(f"Пользователь: {user_info.get('username', 'N/A')}")
            print(f"Email: {user_info.get('email', 'N/A')}")
            print(f"Полное имя: {user_info.get('full_name', 'N/A')}")
        
        # Тест 3: OAuth URLs
        print("\n3️⃣ Тест OAuth URLs:")
        test_oauth_urls()
        
        # Тест 4: Выход
        print("\n4️⃣ Тест выхода:")
        logout(access_token)
    
    else:
        # Если автоматизированная аутентификация не удалась, пробуем автологин
        print("\n2️⃣ Тест автологина:")
        token_data = auto_login()
        
        if not token_data:
            # Тест 3: Регистрация нового пользователя
            print("\n3️⃣ Тест регистрации:")
            test_username = "testuser_" + str(int(time.time()))
            test_email = f"{test_username}@example.com"
            
            sign_up_result = sign_up(
                username=test_username,
                email=test_email,
                password="testpass123!",
                full_name="Test User"
            )
            
            if sign_up_result:
                # Тест 4: Логин с новым пользователем
                print("\n4️⃣ Тест логина:")
                token_data = login_via_password(test_username, "testpass123!")
        
        if token_data:
            access_token = token_data.get('access_token')
            
            # Тест 5: Получение информации о пользователе
            print("\n5️⃣ Тест получения информации о пользователе:")
            user_info = get_current_user(access_token)
            if user_info:
                print(f"Пользователь: {user_info.get('username', 'N/A')}")
                print(f"Email: {user_info.get('email', 'N/A')}")
                print(f"Полное имя: {user_info.get('full_name', 'N/A')}")
            
            # Тест 6: OAuth URLs
            print("\n6️⃣ Тест OAuth URLs:")
            test_oauth_urls()
            
            # Тест 7: Выход
            print("\n7️⃣ Тест выхода:")
            logout(access_token)
    
    print("\n" + "=" * 50)
    print("✅ Тестирование завершено!")

def run_main():
    """Wrapper для запуска async main"""
    import asyncio
    asyncio.run(main())

if __name__ == "__main__":
    import time
    run_main() 