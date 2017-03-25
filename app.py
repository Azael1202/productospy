import web
import model
        
urls = (
    '/', 'Index',
    '/about/(\d+)', 'About',
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
)

t_globas = {
    'datestr': web.datestr
}

render = web.template.render('templates', base='base', globals=t_globas)


class Index:        
    def GET(self):
        posts = model.get_posts()
        return render.index(posts)
        

class About:        
    def GET(self, id):
        post = model.get_post(int(id))
        return render.about(post)


class New:

    form = web.form.Form(

        web.form.Textbox('nombre', web.form.notnull, 
           description="Nomrbe",
            size=30),

        web.form.Textarea('descripcion', web.form.notnull, 
            rows=5, cols=32,
            description="Descripcion: "),

        web.form.Textbox('existencias', web.form.notnull,
            description="Existencias: ",
            size=4),

        web.form.Textbox('precio_compra', web.form.notnull,
            description="Precio de compra: ",
            size=6),

         web.form.Textbox('precio_venta', web.form.notnull,
            description="Precio de venta: ",
            size=6),

          web.form.File('imagen', web.form.notnull,
            size=30,
            description="Imagen del producto:"),

        web.form.Button('Registrar'),
    )

    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        imagen = web.input(imagen_producto={})
        filedir = 'static/imagen'
        filepath = imagen.imagen_producto.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
        fout= open(filedir+'/'+filename,'w')
        fout.write(imagen.imagen_producto.file.read())
        fout.close()
        imagen_producto = filename
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.nombre, form.d.descripcion,form.d.existencias, form.d.precio_compra, form.d.precio_venta, imagen)
        raise web.seeother('/')

class Delete:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.delete(post)

    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')


class Edit:

    def GET(self, id):
        post = model.get_post(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)


    def POST(self, id):
        form = New.form()
        imagen = web.input(imagen_producto={})
        filedir = 'static/images'
        filepath = imagen.imagen.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
        fout= open(filedir+'/'+filename,'w')
        fout.write(imagen.imagen.file.read())
        fout.close()
        imagen = filename
        post = model.get_post(int(id))
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.nombre, form.d.descripcion, form.d.existencias, form.d.precio_compra, form.d.precio_venta, imagen)
        raise web.seeother('/')

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

    