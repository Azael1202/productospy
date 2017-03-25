import web
import MySQLdb

db_host = 'gk90usy5ik2otcvi.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'z8nas5yi6kj6l60w'
db_user = 'vfv4hazwaih2wepv'
db_ps = 't772zrtbejpc3rhb'

db = web.database(
	dbn='mysql',
	host=db_host,
	db=db_name,
	user=db_user,
	pw=db_ps
	)
	

def get_posts():
	return db.select('producto', order='id_producto')

def get_post(id_producto):
	try:
		return db.select('producto', where='id_producto=$id_producto', vars=locals())[0]
	except IndexError:
		return None

def new_post(nombre, descripcion, existencias, precio_compra, precio_venta, imagen_producto):
	db.insert('producto', 
				nombre=nombre, 
				descripcion=descripcion, 
				existencias=existencias, 
				precio_compra=precio_compra, 
				precio_venta=precio_venta, 
				imagen_producto=imagen_producto)

def del_post(id_producto):
	db.delete('producto', where="id_producto=$id_producto", vars=locals())

def update_post(id_producto):
	db.update('producto', where="id_producto=$id_producto", vars=locals(),
	nombre=nombre, descripcion=descripcion, existencias=existencias, precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto=imagen_producto)

def insertar(nombre,descripcion,existencias,precio_compra,precio_venta,imagen_producto):
	db.insert('productos',
		nombre=nombre,
		descripcion= descripcion,
		existencias = existencias, 
		precio_compra= precio_compra,
		precio_venta= precio_venta, 
		imagen_producto= imagen_producto)

#web: python app.py $PORT Procfile sin extencion 
#MySQL-python==1.2.5
#web.py==0.38 .txt