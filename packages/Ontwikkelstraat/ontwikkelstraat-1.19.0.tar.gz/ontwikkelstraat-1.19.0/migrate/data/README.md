Is alleen aanwezig zodat git deze folder meeneemt.

Doel van deze dir is om files in op te kunnen slaan voor het recoveren van de backup.
## unpacken
`xz -vvT 0 -dkf database_to_restore.sql.xz`

één database toevoegen en die hernoemen naar 'database_to_restore.sql'
als die gezipt is via gz KAN je die unzippen via 'gzip -d database_to_restore.sql.gz'
daarna invoke up of invoke whipe-db en daarna invoke up als je als een andere database erin had staan en deze dus wil veranderen naar de nieuwe
