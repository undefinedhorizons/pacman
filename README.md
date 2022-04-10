# pacman

## Струĸтура
Есть карта-лабиринт, коридоры которого заполнены точками. Игрок управляет Пакманом, который ходит по лабиринту и ест точки. В лабиринте также имеются привидения, которые гоняются за героем и хотят убить. В усложненной версии требуется поддержка мультиплеерной игры.

Таким образом, на карте имеются основные объекты четырех типов:
- Игрок (игроки - при выборе мультиплеерной реализации): никнейм, количество жизней, количество очков
- Ограждение лабиринта, все игровые объекта находятся внутри
- Точка, съедаемая только игроком
- Привидение, автоматически двигающееся за игроком

# Детали реализации
Задача игрока — управляя Пакманом, съесть все точки в лабиринте, избегая встречи с привидениями. В начале каждого уровня призраки находятся в недоступной Пакману прямоугольной комнате в середине уровня, из которой они со временем освобождаются. Если привидение дотронется до Пакмана, то его жизнь теряется, призраки и Пакман возвращаются на исходную позицию, но при этом прогресс собранных точек сохраняется. Если при столкновении с призраком у Пакмана не осталось дополнительных жизней, то игра заканчивается. После съедения всех точек начинается новый уровень в том же лабиринте. По бокам лабиринта находятся два входа в один туннель, при вхождении в который Пакман и призраки выходят с другой стороны лабиринта.
