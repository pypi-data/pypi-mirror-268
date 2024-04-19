# Wat is postgres

## Problemen oplossen: 

### Wat als postgres (pg-0, pg-1) niet wil starten? 
Controleer op de volgende foutmelding in `inv up -s pg-0 logs -s pg-0:`
```
[ERROR] PID file "/tmp/repmgrd.pid" exists and seems to contain a valid PID
```
In dat geval: 
```bash 
dc rm pg-0 pg-1 pgpool ; inv up 
```