import mysql.connector 


# db = list()
# database = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
#     host ='informatica.iesquevedo.es',
#     port = 3333,
#     ssl_disabled = True,
#     user ='root', #USUARIO QUE USAMOS NOSOTROS
#     password ='1asir', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
#     database='oscar'
# ) 

# db = list()
database = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='127.0.0.1',
    port = 6033,
    ssl_disabled = True,
    user ='root', #USUARIO QUE USAMOS NOSOTROS
    password ='my_secret_password', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='examen'
) 