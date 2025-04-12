Get-Content "C:\archi-ve\FreeCAD\build\CMakeCache.txt" |
Where-Object {
    ($_ -notmatch '^#') -and
    ($_ -match '^[^/].+:.+=') -and
    ($_ -notmatch 'INTERNAL')
} |
ForEach-Object {
    $parts = ($_ -split '=', 2)
    $key = $parts[0] -split ':', 2
    "-D$($key[0])=$($parts[1])"
} | Set-Content "C:\archi-ve\FreeCAD\tools\build\freecad_flags.txt"