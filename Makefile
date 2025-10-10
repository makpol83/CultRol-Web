# Variables
DB_NAME = cultrol
DB_USER = admin
DB_PASS = TEST
DB_HOST = localhost
DB_PORT = 5432
DB_SCRIPTS = db_management/init.sql db_management/permission_init.sql

# Target por defecto
all: create_db load_tables

# Crear la base de datos
create_db:
	@echo "Creando la base de datos $(DB_NAME)..."
	@PGPASSWORD=$(DB_PASS) createdb -h $(DB_HOST) -p $(DB_PORT) -U $(DB_USER) $(DB_NAME) || echo "La base de datos ya existe"

# Cargar los scripts SQL
load_tables: create_db
	@echo "Cargando scripts SQL en $(DB_NAME)..."
	@for script in $(DB_SCRIPTS); do \
		echo "Ejecutando $$script..."; \
		PGPASSWORD=$(DB_PASS) psql -h $(DB_HOST) -p $(DB_PORT) -U $(DB_USER) -d $(DB_NAME) -f $$script; \
	done

# Limpiar la base de datos
drop_db:
	@echo "Eliminando la base de datos $(DB_NAME)..."
	@PGPASSWORD=$(DB_PASS) dropdb -h $(DB_HOST) -p $(DB_PORT) -U $(DB_USER) $(DB_NAME) || echo "La base de datos no existe"
