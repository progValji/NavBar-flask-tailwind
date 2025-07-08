# NavBar con Flask y Tailwind

El proposito de este pequeño proyecto fue usar los conocimientos que tengo sobre Flask y Tailwind para crear una pequeña pagina web, donde lo que destaca es el menu de navegación. Es el primer menu de Navegacion con interactivdad que creo. 

Me base es una imagen que encotre de una landing page sobre el **Desarrollo Web**.

## Pagina Web
El proyecto cuenta con 4 archivos html ubicados en la carpeta "templates". Los estilos se ubian en la carpeta static y dentros de la carpteta css.
- Pagina de Inicio: Seccion para poder persuadir al usuario de unirse a esta gran experiencia.
- Agenda: Un calendario del mes de Julio del 2025. Se puede dar click a los dias que cuentan con un "*" rojo, se mostrara que se hara ese dia.
- Reseña: Cards de personas, hechas con grid.
- Beneficios: Los beneficios que traera este evento. Hecha con la etiqueta details

## Lo Destacado
Para hacer Navbar con un identifiacdor de que seccion esta actualmente es sumamente facil.
Como estamos usando herencia de Plantillas y tenemos un archivo base que contiene el navbar, en cualquier seccion que visite el usuario siempre estara. Por cada vista creamos una variable y a esa le asignamos el valor de la seccion que esta por visitar, es decir, si el usuario presiona **agenda** la variable tendra el valor de agenda.
~~~py
@app.route('/')
def index():
    seccion = "inicio"
    return render_template('index.html', seccion = seccion)

@app.route('/agenda')
def agenda():
    seccion = "agenda"
    return render_template('agenda.html', seccion = seccion)
~~~

Ahora en nuestro Archivo Base, solo necesitamos comprobar el valor de la variable que nos llega.
~~~html
    <ul>
        <li class="{% if seccion == 'inicio' %}border-b-2{% endif %}">
            <a href="{{ url_for('index') }}" class="{% if seccion == 'inicio' %}font-bold{% endif %}">Inicio</a>
        </li>
    </ul>
~~~
En este caso como identificador estoy haciendo 2 cosas, una es poner el texto en negrita y un border bottom. 
Si **seccion** es inicio entonces se aplican esos estilos. Una forma de dar estilos dependiendo de una condicion, el valor de una variable.

## Áreas de mejora
+ Tailwind es una herramienta poderosa pero como toda herramienta, hay que saber en que momentos utilizarla. Realmente no se si para este pequeño proyecto estuvo bien, ya que en una plantilla escribi un poco de CSS puro.

+ Seguir practicando el Responsive Design.
 
+ Mejorar la semantica de HTML