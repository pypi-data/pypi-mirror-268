# Wat is invoke 
Zie ook:
 * [pip.compile](wat-is-pip-compile.md) en
 * [bundle.build](wat-is-de-bundler.md)
 * [backup en restore met invoke](hoe-werkt-de-backup-en-restore.md)
 * https://www.pyinvoke.org 

# Invoke UP
Brengt de service van de omgeving (uiteindelijk) online.

In de feature backend omgeving, rekent hij de hash uit van de shared code, wat gebruikt wordt 
voor de flag file van migrate. Dat betekent dat bij een update van de core library files, een 
verandering in de hash optreed, en een andere migrate flag gebruikt wordt om te kijken of de 
migrate al is uitgevoerd, zodat bij wijziging van code we verplichten dat de migrate *wordt* 
uitgevoerd. 

De migrate kijkt vervolgens zelf of er nog updates gedaan moeten worden aan de databse, of dat 
er uberhaupt een backup recovered moet worden. 


# 