import psycopg2

#Hacer la conexion a la base de datos
conexion = psycopg2.connect(
    host = "localhost", 
    port =  "5432",
    database = "credenciales",
    user = "Admin",
    password = "p4ssw0rdDB"
)


#2 Crear el cursor

cursor = conexion.cursor()

#3 Ejecutar la consulta
cursor.execute("SELECT * FROM usuarios")
registros = cursor.fetchall()

#4 Mostrar resultados
for fila in registros:
    print(fila)

#5 Cerrar las conexiones
cursor.close()
conexion.close()
