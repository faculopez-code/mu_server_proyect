mu-server-project/
├── MuServer/                  # El core del servidor MUEMU
│   ├── GameServer.exe
│   ├── Data/
│   └── Configs/
│
├── Cliente/                   # Cliente que se entrega a los jugadores
│   ├── main.exe
│   ├── data/
│   └── launcher.exe
│
├── docker/                    # Archivos y scripts Docker
│   ├── docker-compose.yml
│   ├── sqlserver/             # Persistencia, init scripts o backups
│   └── wine-gameserver/       # Dockerfile con GameServer si querés contenerizarlo
│
├── python-tools/              # Scripts útiles de administración
│   ├── backup.py
│   ├── reset_manager.py
│   └── connect_sql_test.py
│
├── web-panel/                 # Web de administración o sitio del servidor
│   ├── app.py                 # (si usás Flask o Node.js)
│   ├── templates/
│   └── static/
│
├── README.md                  # Documentación del proyecto
└── .env                       # Variables sensibles (IP SQL, claves)
