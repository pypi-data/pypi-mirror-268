#!/usr/bin/env python3

import os


def setup_env_file():
    """
    Configura y crea un archivo .env con las credenciales para la conexión a la base de datos.

    Solicita al usuario que introduzca los detalles necesarios para la conexión a la base de datos,
    incluyendo el controlador, host, nombre de la base de datos, usuario y contraseña. Si el usuario
    no especifica un controlador, se utiliza un valor predeterminado.

    Ejemplo de uso:
    ---------------
    setup_env_file()  # Pide al usuario los detalles y crea el archivo .env
    """
    default_db_driver = "ODBC Driver 18 for SQL Server"
    print(f"The default database driver is '{default_db_driver}'.")
    db_driver = input(
        "Press Enter to accept the default, or specify a different driver: "
    ).strip()
    db_driver = db_driver if db_driver else default_db_driver
    db_host = input("Enter the database host (e.g., localhost): ").strip()
    db_database = input("Enter the database name: ").strip()
    db_username = input("Enter the database username: ").strip()
    db_password = input("Enter the database password: ").strip()

    env_content = f"""# Database configuration
                        DB_DRIVER='{db_driver}'
                        DB_HOST='{db_host}'
                        DB_DATABASE='{db_database}'
                        DB_USERNAME='{db_username}'
                        DB_PASSWORD='{db_password}'
                    """
    with open(".env", "w") as env_file:
        env_file.write(env_content)
    print(".env file created with your provided details.")


def create_dirs(base_path, dirs_list):
    """
    Crea directorios en la ruta base especificada si no existen.

    Parámetros:
    -----------
    base_path (str): La ruta base donde se crearán los directorios.
    dirs_list (list): Una lista de nombres de directorios a crear.

    Ejemplo de uso:
    ---------------
    create_dirs('/path/to/project', ['data', 'logs'])  # Crea directorios en la ruta especificada
    """
    for dir_name in dirs_list:
        dir_path = os.path.join(base_path, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory {dir_path} created.")


def main():
    """
    Ejecuta las tareas de configuración inicial para preparar el entorno de operación del paquete.

    Realiza la configuración inicial del archivo .env para almacenar las credenciales de la base de datos y crea
    directorios necesarios para el funcionamiento del paquete. Informa al usuario una vez que la configuración
    está completa.

    Ejemplo:
    --------
    import first_run
    first_run.main()  # Configura el entorno inicial y crea directorios necesarios
    """
    project_root = os.getcwd()
    setup_env_file()
    directories = ["data", "data/raw", "data/export"]
    create_dirs(project_root, directories)
    print("Setup completed successfully.")


if __name__ == "__main__":
    main()
