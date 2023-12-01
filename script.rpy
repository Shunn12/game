#Personajes 
define Cath = Character ("Catherine", color = "#57a64b")
define Arth = Character("Arthur", color ="#e88e3a")
define Ad = Character("Adam", color ="#363da8")
define Gwen = Character("Gwen", color ="#e38dac")
define Mc = Character("[NomUs]", color ="#bdccff")

$NomUs = ""

#imagenes en uso
image cielo = "bg cielo.jpg"
image club = "bg club.jpg"
image me = "bg meadow.jpg"
image lec = "bg lecturehall.jpg"
image uni = "bg uni.jpg"
image Catherine = "Catherine.png"
image catcon = "catcon.png"
image catfeliz = "catfeliz.png"
image Art = "arthur.png"
image Artcon = "artcon.png"
image Artfeliz = "artfeliz.png"
image Ad = "adam.png"
image Adcon = "adcon.png"
image Adfeliz="adf.png"
image Gwen = "gwen.png"
image Gwencon ="gwencon.png"
image Gwenfeliz = "gwenf.png"
image depa = "bg depa.jpg"
image tienda = "bg tienda.jpg"
image par = "bg parada.jpg"

#Inicia The "707"
label start:
    #Musica
    play music "audio/MM.mp3"

    #Colocar fondo
    scene cielo
    
    #Variable de nombre personalizado
    $NomUs = renpy.input ("Dime tu nombre.")
    "Me gusta tu nombre [NomUs]."

    "Bienvenida a 'The 707', nos alegra que hayas entrado a nuestro juego.\nAquí te ayudaremos a mejorar en lo que desees."
    "Dime [NomUs]¿Con quien te gustaria empezar?\nPor favor, escoja una opción."

    #Respuestas
    menu:

        "Catherine. (Amable)":

            jump Cathe

        "Arthur. (Respeto)":

            jump Arthur
        "Adam. (Modales)":

            jump Adam

        "Gwen. (Interactuar)":

            jump Gwen
    return
    hide cielo

    #Opciones de las respuestas
    label Cathe: 
        scene cielo
        "Perfecto.\nPor favor, dejame contarte un poco de [NomUs]."
        "[NomUs] es una jovén, que está por comenzar su primer año en la universidad."
        "Luego de ser aceptada, comenzó a trabajar medio tiempo. Recaudando un poco para comenzar la universidad."
        "Ya que al vivir sola, tiene que ver como hará para arreglarselas."
        "Dicho esto, disfruta el juego."

        show uni with fade

        Mc "(Era un día bastante tranquilo, y el clima estaba un poco caluroso... sin embargo era soportable.)"
        Mc "\[Yo me dirigía hacia la universidad, puesto que las clases habian empezado.\]"
        
        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "(En el camino, pude ver un rostro familiar. Era Catherine, una compañera de la secundaria. Ha pasado un tiempo desde que la ví.)"
        Mc "(Como estuve ocupada trabajando, no pude visitarla... Iré a saludarle.)"
        Mc "\[Me acerqué lo suficiente como para que notara mi presencia.\]"
        Mc "\[Noté como su rostro formó una pequeña sonrisa al verme.\]"
        Cath "[NomUs], cuánto tiempo sin verte. ¿Cómo has estado?"
        
        hide catherine

        menu:
            "Hola, Catherine. Me encuentro bien. ¿Tú?":
                jump a
            
            "...Bien, supongo.":
                jump b

            "\[Ignorar y continuar.\]":
                jump c
        return
    return    
        
    label a:
        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "Estoy bien, es bueno verte luego de tanto ¿Te diriges a la universidad?"
        Mc "Sí, justo estoy yendo para allá. ¿También estabas por ir? Si es así, podemos ir juntas."

        show catfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "Eso sería genial, en el camino pdorías contarme sobre tu trabajo."

        hide catfeliz

        Cath "Bueno, si tú quieres."
        Mc "\[Comencé a contarle sobre mi trabajo, el cual era dentro de todo bueno... Lastima que no pude hacer otra cosa más que trabajar.\]"
        Mc "\[Pude ver a Catherine con una cara melancolica.\]"
        Mc "¿Ocurré algo?"

        show catcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
            
        Cath "Bueno... Me hubiera gustado haberte visitado."
        
        Mc "Está bien, cada una estaba en lo suyo."
        
        hide catcon
        
        Cath "Aún así, perdí la oportunidad de acomprañarte cuando lo necesites..."
        
        Mc "Está bien, de verdad."
        Mc "\[Le dí unas palmaditas en la espalda.\]"
        Mc "(Luego de eso, llegamos a la univerdad.)"
        hide catcon
        scene lec with fade

        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
                
        menu:
            "Ensalada.":
                jump ensalada
            
            "Sandwich.":
                jump sand
            
            "Saltearse el almuerzo.":
                jump salt
        return

    return
    label ensalada:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Catherine por pedir.)"

        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "[NomUs], nos volvemos a encontrar."

        show catfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide catfeliz

        Cath "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Cath "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Cath "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Cath "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Catherine comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide catherine
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Cath, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide catfeliz
        hide catherine

    return
    label sand:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Catherine por pedir.)"

        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "[NomUs], nos volvemos a encontrar."

        show catfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide catfeliz

        Cath "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Cath "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Cath "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Cath " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Cath "\[Catherine comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide catherine

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Cath, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide catfeliz
        hide catherine
    return
    label salt:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Catherine.\]"

        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Catherine. Sí, ya me estoy por volver."
        
        show catcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Cath "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide catcon

        Mc "Aww, es tierno que te preocupes por mi."

        Cath "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show catfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Catherine parecia feliz por mi respuesta.\]"
        Mc "(Catherine tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide catfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Cath, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide catfeliz
        hide catherine
    return
    label b: 
        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        
        Cath "Oh, ¿Te ha ocurrido algo? Puedes contarme, si lo deseas."
        
        Mc "Es solo que el trabajo no me ha dejado disfrutar mucho el verano... y ahora no tendré mucho tiempo por la univerdad."
        
        Cath "Ya veo... Lamento que las cosas sean asi para ti. Desearía poder ayudarte de alguna manera.¿Te gustaría que nos juntemos a charlar?"
        
        Mc "Muchas gracias, Catherine.\nCon gusto aceptaré tu invitación."
        Mc "(Mientras nos dirigiamos a la universidad, Catherine intentó animarme y me puse mejor gracias a ella.)"
        scene uni
        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        scene lec
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
        hide catherine
        menu:
            "Ensalada.":
                jump ensalada1
            
            "Sandwich.":
                jump sand1
            
            "Saltearse el almuerzo.":
                jump salt1
        return

    return
    label ensalada1:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Catherine por pedir.)"

        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "[NomUs], nos volvemos a encontrar."

        show catfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide catfeliz

        Cath "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Cath "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Cath "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Cath "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Catherine comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide catherine
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Cath, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide catfeliz
        hide catherine

    return
    label sand1:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Catherine por pedir.)"

        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "[NomUs], nos volvemos a encontrar."

        show catfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide catfeliz

        Cath "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Cath "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Cath "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Cath " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Cath "\[Catherine comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide catherine

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Cath, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide catfeliz
        hide catherine
    return
    label salt1:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Catherine.\]"

        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Catherine. Sí, ya me estoy por volver."
        
        show catcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Cath "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide catcon

        Mc "Aww, es tierno que te preocupes por mi."

        Cath "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show catfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Catherine parecia feliz por mi respuesta.\]"
        Mc "(Catherine tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide catfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Cath, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide catfeliz
        hide catherine
    return
    return

    label c:
        show catcon with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
        Mc "(Supongo que me ganaron los nervios, y mi cuerpo actuó por cuenta propia...)"
        
        hide catcon

        Mc "(Pude ver el rostro de Catherine, tenía una expresión de confunción, mezclada con decepción.)"
        Mc  "\[Me dirigí a la universidad, intentando olvidar lo ocurrido.\]"
        scene uni
        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        scene lec
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
        hide catherine
        menu:
            "Ensalada.":
                jump ensalada2
            
            "Sandwich.":
                jump sand2
            
            "Saltearse el almuerzo.":
                jump salt2
        return

    return
    label ensalada2:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Catherine por pedir.)"

        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "[NomUs], nos volvemos a encontrar."

        show catfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide catfeliz

        Cath "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Cath "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Cath "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Cath "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Catherine comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide catherine
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Cath, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide catfeliz
        hide catherine

    return
    label sand2:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Catherine por pedir.)"

        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "[NomUs], nos volvemos a encontrar."

        show catfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide catfeliz

        Cath "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Cath "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Cath "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Cath " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Cath "\[Catherine comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide catherine

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Cath, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide catfeliz
        hide catherine
    return
    label salt2:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Catherine.\]"

        show catherine with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Catherine. Sí, ya me estoy por volver."
        
        show catcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Cath "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Cath "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide catcon

        Mc "Aww, es tierno que te preocupes por mi."

        Cath "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show catfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Catherine parecia feliz por mi respuesta.\]"
        Mc "(Catherine tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide catfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Cath, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide catfeliz
        hide catherine
    return
    return

    label Arthur: 
        scene cielo
        "Perfecto.\nPor favor, dejame contarte un poco de [NomUs]."
        "[NomUs] es una jovén, que está por comenzar su primer año en la universidad."
        "Luego de ser aceptada, comenzó a trabajar medio tiempo. Recaudando un poco para comenzar la universidad."
        "Ya que al vivir sola, tiene que ver como hará para arreglarselas."
        "Dicho esto, disfruta el juego."

        show uni with fade

        Mc "(Era un día bastante tranquilo, y el clima estaba un poco caluroso... sin embargo era soportable.)"
        Mc "\[Yo me dirigía hacia la universidad, puesto que las clases habian empezado.\]"
        
        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "(En el camino, pude ver un rostro familiar. Era Arthur, una compañera de la secundaria. Ha pasado un tiempo desde que la ví.)"
        Mc "(Como estuve ocupada trabajando, no pude visitarla... Iré a saludarle.)"
        Mc "\[Me acerqué lo suficiente como para que notara mi presencia.\]"
        Mc "\[Noté como su rostro formó una pequeña sonrisa al verme.\]"
        Arth "[NomUs], cuánto tiempo sin verte. ¿Cómo has estado?"
        
        hide art

        menu:
            "Hola, Arthur. Me encuentro bien. ¿Tú?":
                jump a1
            
            "...Bien, supongo.":
                jump b1

            "\[Ignorar y continuar.\]":
                jump c1
        return
    return    
        
    label a1:
        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "Estoy bien, es bueno verte luego de tanto ¿Te diriges a la universidad?"
        Mc "Sí, justo estoy yendo para allá. ¿También estabas por ir? Si es así, podemos ir juntas."

        show artfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "Eso sería genial, en el camino pdorías contarme sobre tu trabajo."

        hide artfeliz

        Arth "Bueno, si tú quieres."
        Mc "\[Comencé a contarle sobre mi trabajo, el cual era dentro de todo bueno... Lastima que no pude hacer otra cosa más que trabajar.\]"
        Mc "\[Pude ver a Arthur con una cara melancolica.\]"
        Mc "¿Ocurré algo?"

        show artcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
            
        Arth "Bueno... Me hubiera gustado haberte visitado."
        
        Mc "Está bien, cada una estaba en lo suyo."
        
        hide artcon
        
        Arth "Aún así, perdí la oportunidad de acomprañarte cuando lo necesites..."
        
        Mc "Está bien, de verdad."
        Mc "\[Le dí unas palmaditas en la espalda.\]"
        Mc "(Luego de eso, llegamos a la univerdad.)"
        hide artcon
        scene lec with fade

        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
                
        menu:
            "Ensalada.":
                jump ensalada3
            
            "Sandwich.":
                jump sand3
            
            "Saltearse el almuerzo.":
                jump salt3
        return

    return
    label ensalada3:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Arthur por pedir.)"

        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "[NomUs], nos volvemos a encontrar."

        show artfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide artfeliz

        Arth "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Arth "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Arth "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Arth "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Arthur comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide art
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Arthur, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide artfeliz
        hide art

    return
    label sand3:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Arthur por pedir.)"

        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "[NomUs], nos volvemos a encontrar."

        show artfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide artfeliz

        Arth "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Arth "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Arth "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Arth " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Arth "\[Arthur comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide art

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Arthur, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide artfeliz
        hide art
    return
    label salt3:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Arthur.\]"

        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Arthur. Sí, ya me estoy por volver."
        
        show artcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Arth "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide artcon

        Mc "Aww, es tierno que te preocupes por mi."

        Arth "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show artfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Arthur parecia feliz por mi respuesta.\]"
        Mc "(Arthur tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide artfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Arthur, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide artfeliz
        hide art
    return
    label b1: 
        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        
        Arth "Oh, ¿Te ha ocurrido algo? Puedes contarme, si lo deseas."
        
        Mc "Es solo que el trabajo no me ha dejado disfrutar mucho el verano... y ahora no tendré mucho tiempo por la univerdad."
        
        Arth "Ya veo... Lamento que las cosas sean asi para ti. Desearía poder ayudarte de alguna manera.¿Te gustaría que nos juntemos a charlar?"
        
        Mc "Muchas gracias, Arthur.\nCon gusto aceptaré tu invitación."
        Mc "(Mientras nos dirigiamos a la universidad, Arthur intentó animarme y me puse mejor gracias a ella.)"
        scene uni
        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        scene lec
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
        hide art
        menu:
            "Ensalada.":
                jump ensalada4
            
            "Sandwich.":
                jump sand4
            
            "Saltearse el almuerzo.":
                jump salt4
        return

    return
    label ensalada4:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Arthur por pedir.)"

        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "[NomUs], nos volvemos a encontrar."

        show artfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide artfeliz

        Arth "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Arth "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Arth "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Arth "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Arthur comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide art
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Arthur, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide artfeliz
        hide art

    return
    label sand4:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Arthur por pedir.)"

        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "[NomUs], nos volvemos a encontrar."

        show artfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide artfeliz

        Arth "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Arth "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Arth "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Arth " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Arth "\[Arthur comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide art

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Arthur, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide artfeliz
        hide art
    return
    label salt4:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Arthur.\]"

        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Arthur. Sí, ya me estoy por volver."
        
        show artcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Arth "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide artcon

        Mc "Aww, es tierno que te preocupes por mi."

        Arth "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show artfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Arthur parecia feliz por mi respuesta.\]"
        Mc "(Arthur tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide artfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Arthur, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide artfeli
        hide art
    return
    return

    label c1:
        show artcon with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
        Mc "(Supongo que me ganaron los nervios, y mi cuerpo actuó por cuenta propia...)"
        
        hide artcon

        Mc "(Pude ver el rostro de Arthur, tenía una expresión de confunción, mezclada con decepción.)"
        Mc  "\[Me dirigí a la universidad, intentando olvidar lo ocurrido.\]"
        scene uni
        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        scene lec
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
        hide art
        menu:
            "Ensalada.":
                jump ensalada5
            
            "Sandwich.":
                jump sand5
            
            "Saltearse el almuerzo.":
                jump salt5
        return

    return
    label ensalada5:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Arthur por pedir.)"

        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "[NomUs], nos volvemos a encontrar."

        show artfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide artfeliz

        Arth "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Arth "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Arth "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Arth "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Arthur comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide art
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Arthur, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide artfeliz
        hide art

    return
    label sand5:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Arthur por pedir.)"

        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "[NomUs], nos volvemos a encontrar."

        show artfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide artfeliz

        Arth "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Arth "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Arth "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Arth " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Arth "\[Arthur comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide art

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Arthur, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide artfeliz
        hide art
    return
    label salt5:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Arthur.\]"

        show art with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Arthur. Sí, ya me estoy por volver."
        
        show artcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Arth "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Arth "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide artcon

        Mc "Aww, es tierno que te preocupes por mi."

        Arth "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show artfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Arthur parecia feliz por mi respuesta.\]"
        Mc "(Arthur tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide artfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Arthur, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide artfeliz
        hide art
    return
    return

    label Adam: 
        scene cielo
        "Perfecto.\nPor favor, dejame contarte un poco de [NomUs]."
        "[NomUs] es una jovén, que está por comenzar su primer año en la universidad."
        "Luego de ser aceptada, comenzó a trabajar medio tiempo. Recaudando un poco para comenzar la universidad."
        "Ya que al vivir sola, tiene que ver como hará para arreglarselas."
        "Dicho esto, disfruta el juego."

        show uni with fade

        Mc "(Era un día bastante tranquilo, y el clima estaba un poco caluroso... sin embargo era soportable.)"
        Mc "\[Yo me dirigía hacia la universidad, puesto que las clases habian empezado.\]"
        
        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "(En el camino, pude ver un rostro familiar. Era Arthur, una compañera de la secundaria. Ha pasado un tiempo desde que la ví.)"
        Mc "(Como estuve ocupada trabajando, no pude visitarla... Iré a saludarle.)"
        Mc "\[Me acerqué lo suficiente como para que notara mi presencia.\]"
        Mc "\[Noté como su rostro formó una pequeña sonrisa al verme.\]"
        Ad "[NomUs], cuánto tiempo sin verte. ¿Cómo has estado?"
        
        hide Ad

        menu:
            "Hola, Arthur. Me encuentro bien. ¿Tú?":
                jump a2
            
            "...Bien, supongo.":
                jump b2

            "\[Ignorar y continuar.\]":
                jump c2
        return
    return    
        
    label a2:
        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "Estoy bien, es bueno verte luego de tanto ¿Te diriges a la universidad?"
        Mc "Sí, justo estoy yendo para allá. ¿También estabas por ir? Si es así, podemos ir juntas."

        show Adfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "Eso sería genial, en el camino pdorías contarme sobre tu trabajo."

        hide Adfeliz

        Ad "Bueno, si tú quieres."
        Mc "\[Comencé a contarle sobre mi trabajo, el cual era dentro de todo bueno... Lastima que no pude hacer otra cosa más que trabajar.\]"
        Mc "\[Pude ver a Adam con una cara melancolica.\]"
        Mc "¿Ocurré algo?"

        show Adcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
            
        Ad "Bueno... Me hubiera gustado haberte visitado."
        
        Mc "Está bien, cada una estaba en lo suyo."
        
        hide Adcon
        
        Ad "Aún así, perdí la oportunidad de acomprañarte cuando lo necesites..."
        
        Mc "Está bien, de verdad."
        Mc "\[Le dí unas palmaditas en la espalda.\]"
        Mc "(Luego de eso, llegamos a la univerdad.)"
        hide Adcon
        scene lec with fade

        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
                
        menu:
            "Ensalada.":
                jump ensalada6
            
            "Sandwich.":
                jump sand6
            
            "Saltearse el almuerzo.":
                jump salt6
        return

    return
    label ensalada6:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Adam por pedir.)"

        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "[NomUs], nos volvemos a encontrar."

        show Adfleiz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Adfeliz

        Ad "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Ad "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Ad "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Ad "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Adam comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide Ad
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Adam, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Adfeliz
        hide Ad

    return
    label sand6:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Adam por pedir.)"

        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "[NomUs], nos volvemos a encontrar."

        show Adfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Adfeliz

        Ad "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Ad "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Ad "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Ad " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Ad "\[Adam comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide Ad

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Adam, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Adfeliz
        hide Ad
    return
    label salt6:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Adam.\]"

        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Adam. Sí, ya me estoy por volver."
        
        show Adcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Ad "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide Adcon

        Mc "Aww, es tierno que te preocupes por mi."

        Ad "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show Adfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Adam parecia feliz por mi respuesta.\]"
        Mc "(Adam tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide Adfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Adam, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Adfeliz
        hide Adherine
    return
    label b2: 
        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        
        Ad "Oh, ¿Te ha ocurrido algo? Puedes contarme, si lo deseas."
        
        Mc "Es solo que el trabajo no me ha dejado disfrutar mucho el verano... y ahora no tendré mucho tiempo por la univerdad."
        
        Ad "Ya veo... Lamento que las cosas sean asi para ti. Desearía poder ayudarte de alguna manera.¿Te gustaría que nos juntemos a charlar?"
        
        Mc "Muchas gracias, Adam.\nCon gusto aceptaré tu invitación."
        Mc "(Mientras nos dirigiamos a la universidad, Adam intentó animarme y me puse mejor gracias a ella.)"
        scene uni
        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        scene lec
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
        hide Ad
        menu:
            "Ensalada.":
                jump ensalada7
            
            "Sandwich.":
                jump sand7
            
            "Saltearse el almuerzo.":
                jump salt7
        return

    return
    label ensalada7:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Adam por pedir.)"

        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "[NomUs], nos volvemos a encontrar."

        show Adfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Adfeliz

        Ad "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Ad "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Ad "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Ad "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Adam comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide Ad
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Adam, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Adfeliz
        hide Ad

    return
    label sand7:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Adam por pedir.)"

        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "[NomUs], nos volvemos a encontrar."

        show Adfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Adfeliz

        Ad "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Ad "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Ad "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Ad " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Ad "\[Adam comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide Ad

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Ad, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Adfeliz
        hide Ad
    return
    label salt7:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Adam.\]"

        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Adam. Sí, ya me estoy por volver."
        
        show Adcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Ad "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide Adcon

        Mc "Aww, es tierno que te preocupes por mi."

        Ad "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show Adfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Adam parecia feliz por mi respuesta.\]"
        Mc "(Adam tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide Adfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Adam, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Adfeliz
        hide Ad
    return
    return

    label c2:
        show cAdcon with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
        Mc "(Supongo que me ganaron los nervios, y mi cuerpo actuó por cuenta propia...)"
        
        hide Adcon

        Mc "(Pude ver el rostro de Adam, tenía una expresión de confunción, mezclada con decepción.)"
        Mc  "\[Me dirigí a la universidad, intentando olvidar lo ocurrido.\]"
        scene uni
        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        scene lec
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
        hide Ad
        menu:
            "Ensalada.":
                jump ensalada8
            
            "Sandwich.":
                jump sand8
            
            "Saltearse el almuerzo.":
                jump salt8
        return

    return
    label ensalada8:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Adam por pedir.)"

        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "[NomUs], nos volvemos a encontrar."

        show Adfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Adfeliz

        Ad "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Ad "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Ad "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Ad "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Adam comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide Ad
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Adam, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Adfeliz
        hide Ad

    return
    label sand8:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Adam por pedir.)"

        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "[NomUs], nos volvemos a encontrar."

        show Adfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Adfeliz

        Ad "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Ad "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Ad "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Ad " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Ad "\[Adam comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide Ad

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Adam, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Adfeliz
        hide Ad
    return
    label salt8:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Adam.\]"

        show Ad with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Adam. Sí, ya me estoy por volver."
        
        show Adcon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Ad "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Ad "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide Adcon

        Mc "Aww, es tierno que te preocupes por mi."

        Ad "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show Adfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Adam parecia feliz por mi respuesta.\]"
        Mc "(Adam tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide Adfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Adam, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Adfeliz
        hide Ad
    return
    return

    label Gwen: 
        scene cielo
        "Perfecto.\nPor favor, dejame contarte un poco de [NomUs]."
        "[NomUs] es una jovén, que está por comenzar su primer año en la universidad."
        "Luego de ser aceptada, comenzó a trabajar medio tiempo. Recaudando un poco para comenzar la universidad."
        "Ya que al vivir sola, tiene que ver como hará para arreglarselas."
        "Dicho esto, disfruta el juego."

        show uni with fade

        Mc "(Era un día bastante tranquilo, y el clima estaba un poco caluroso... sin embargo era soportable.)"
        Mc "\[Yo me dirigía hacia la universidad, puesto que las clases habian empezado.\]"
        
        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "(En el camino, pude ver un rostro familiar. Era Gwen, una compañera de la secundaria. Ha pasado un tiempo desde que la ví.)"
        Mc "(Como estuve ocupada trabajando, no pude visitarla... Iré a saludarle.)"
        Mc "\[Me acerqué lo suficiente como para que notara mi presencia.\]"
        Mc "\[Noté como su rostro formó una pequeña sonrisa al verme.\]"
        Gwen "[NomUs], cuánto tiempo sin verte. ¿Cómo has estado?"
        
        hide Gwen

        menu:
            "Hola, Gwen. Me encuentro bien. ¿Tú?":
                jump a3
            
            "...Bien, supongo.":
                jump b3

            "\[Ignorar y continuar.\]":
                jump c3
        return
    return    
        
    label a3:
        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "Estoy bien, es bueno verte luego de tanto ¿Te diriges a la universidad?"
        Mc "Sí, justo estoy yendo para allá. ¿También estabas por ir? Si es así, podemos ir juntas."

        show Gwenfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "Eso sería genial, en el camino pdorías contarme sobre tu trabajo."

        hide Gwen

        Gwen "Bueno, si tú quieres."
        Mc "\[Comencé a contarle sobre mi trabajo, el cual era dentro de todo bueno... Lastima que no pude hacer otra cosa más que trabajar.\]"
        Mc "\[Pude ver a Gwen con una cara melancolica.\]"
        Mc "¿Ocurré algo?"

        show Gwencon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
            
        Gwen "Bueno... Me hubiera gustado haberte visitado."
        
        Mc "Está bien, cada una estaba en lo suyo."
        
        hide Gwencon
        
        Gwen "Aún así, perdí la oportunidad de acomprañarte cuando lo necesites..."
        
        Mc "Está bien, de verdad."
        Mc "\[Le dí unas palmaditas en la espalda.\]"
        Mc "(Luego de eso, llegamos a la univerdad.)"
        hide Gwencon
        scene lec with fade

        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
                
        menu:
            "Ensalada.":
                jump ensalada9
            
            "Sandwich.":
                jump sand9
            
            "Saltearse el almuerzo.":
                jump salt9
        return

    return
    label ensalada9:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Gwen por pedir.)"

        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "[NomUs], nos volvemos a encontrar."

        show Gwenfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Gwenfeliz

        Gwen "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Gwen "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Gwen "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Gwen "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Gwen comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide Gwen
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Gwen, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Gwenfeliz
        hide Gwenherine

    return
    label sand9:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Gwen por pedir.)"

        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "[NomUs], nos volvemos a encontrar."

        show Gwenfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Gwenfeliz

        Gwen "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Gwen "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Gwen "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Gwen " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Gwen "\[Gwen comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide Gwen

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Gwen, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Gwenfeliz
        hide Gwen
    return
    label salt9:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Gwen.\]"

        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Gwen. Sí, ya me estoy por volver."
        
        show Gwencon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Gwen "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide Gwencon

        Mc "Aww, es tierno que te preocupes por mi."

        Gwen "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show Gwenfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Gwen parecia feliz por mi respuesta.\]"
        Mc "(Gwen tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide Gwenfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Gwen, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Gwenfeliz
        hide Gwen
    return
    label b3: 
        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        
        Gwen "Oh, ¿Te ha ocurrido algo? Puedes contarme, si lo deseas."
        
        Mc "Es solo que el trabajo no me ha dejado disfrutar mucho el verano... y ahora no tendré mucho tiempo por la univerdad."
        
        Gwen "Ya veo... Lamento que las cosas sean asi para ti. Desearía poder ayudarte de alguna manera.¿Te gustaría que nos juntemos a charlar?"
        
        Mc "Muchas gracias, Gwen.\nCon gusto aceptaré tu invitación."
        Mc "(Mientras nos dirigiamos a la universidad, Gwen intentó animarme y me puse mejor gracias a ella.)"
        scene uni
        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        scene lec
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
        hide Gwen
        menu:
            "Ensalada.":
                jump ensalada10
            
            "Sandwich.":
                jump sand10
            
            "Saltearse el almuerzo.":
                jump salt10
        return

    return
    label ensalada10:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Gwen por pedir.)"

        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "[NomUs], nos volvemos a encontrar."

        show Gwenfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Gwenfeliz

        Gwen "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Gwen "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Gwen "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Gwen "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Gwen comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide Gwen
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Gwen, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Gwenfeliz
        hide Gwen

    return
    label sand10:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Gwen por pedir.)"

        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "[NomUs], nos volvemos a encontrar."

        show Gwenfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Gwenfeliz

        Gwen "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Gwen "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Gwen "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Gwen " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Gwen "\[Gwen comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide Gwen

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Gwen, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Gwenfeliz
        hide Gwen
    return
    label salt10:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Gwen.\]"

        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Gwen. Sí, ya me estoy por volver."
        
        show Gwencon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Gwen "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide Gwencon

        Mc "Aww, es tierno que te preocupes por mi."

        Gwen "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show Gwenfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Gwen parecia feliz por mi respuesta.\]"
        Mc "(Gwen tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide Gwenfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Gwen, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Gwenfeliz
        hide Gwen
    return
    return

    label c3:
        show Gwencon with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
        Mc "(Supongo que me ganaron los nervios, y mi cuerpo actuó por cuenta propia...)"
        
        hide Gwencon

        Mc "(Pude ver el rostro de Gwen, tenía una expresión de confunción, mezclada con decepción.)"
        Mc  "\[Me dirigí a la universidad, intentando olvidar lo ocurrido.\]"
        scene uni
        Mc "\[Estando en la universidad, me dirigí a mi salón asignado.\]"
        scene lec
        Mc "(Ya en el salón comenzaron a dar clases, así que comencé a tomar notas.)"
        Mc "(Luego de un largo día, ya era hora de almorzar algo.)"
        Mc "¿Que debería almorzar?"
        hide Gwen
        menu:
            "Ensalada.":
                jump ensalada11
            
            "Sandwich.":
                jump sand11
            
            "Saltearse el almuerzo.":
                jump salt11
        return

    return
    label ensalada11:
        Mc "(Supongo que algo saludable sería lo mejor.)"
        Mc "\[Comencé a buscar una tienda para comprar algo sencillo de almorzar.\]"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Gwen por pedir.)"

        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "[NomUs], nos volvemos a encontrar."

        show Gwenfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Gwenfeliz

        Gwen "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Gwen "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Gwen "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo quería algo sencillo, así que iba a pedir una ensalada."

        Gwen "Si no sabés cúal elegir, puedo ayudarte."

        Mc "Muchas gracias."
        Mc "\[Gwen comenzó  a sugerirme algunas ensaladas. Al final opté por una que contiene: lechuga, tomate cherry, pepinillos, y pollo.\]"
        Mc "Terminamos teniendo una charla en lo que almorzabamos, fue agradable estar almorzando con alguien."
        
        hide Gwen
        
        Mc "\[Al terminar, nos despedimos y volvimos a lo nuestro.\]"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Gwen, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Gwenfeliz
        hide Gwen

    return
    label sand11:
        Mc "(Supongo que algo sencillo sería lo mejor)"
        scene tienda
        Mc "(Logré encontrar un lugar cerca de la universidad, así que entré.\nAl parecer tambien se encontraba Gwen por pedir.)"

        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "[NomUs], nos volvemos a encontrar."

        show Gwenfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Mc "Así parece. ¿Ya estabas por ordenar?"

        hide Gwenfeliz

        Gwen "Sí, escuché que aquí vendian almuerzos vegetarianos."

        Mc "Vaya, que bueno, te queda muy bien.\n¿Ya pensaste que pedirás?"

        Gwen "Así es. Hay un platillo que contiene fideos con champiniones a la crema."

        Mc "Wow, suena muy delicioso."

        Gwen "Sí, sí. ¿Tú qué pedirás?"

        Mc "Bueno, yo queria algo sencillo, así que iba a pedir un sandwich."

        Gwen " Si no sabes que elegir, puedo ayudarte."

        Mc "Muchas gracias."

        Gwen "\[Gwen comenzó a sugerirme algunos sandwiches. Al final opté por uno con: Huevo, lechuga, jamón y queso.\]"

        hide Gwen

        Mc "(Terminamos teniendo una charla en lo que almorzabamos, fue agrabale almorzar junto con alguien.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Gwen, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"no ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Gwenfeliz
        hide Gwen
    return
    label salt11:
        scene me with fade
        Mc "(Supongo que no tengo apetito por ahora...)"
        scene par with fade
        Mc "\[Comencé a caminar a la parada del colectivo.\]"
        Mc "(Al llegar, me senté y me propuse esperar.\n Sin embargo, alguien tocó mi hombro, llamandome.)"
        Mc "\[Al voltear, pude ver a Gwen.\]"

        show Gwen with fade:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "[NomUs], me alegra encontrarte. ¿Ya te iras?"

        Mc "Ah, Gwen. Sí, ya me estoy por volver."
        
        show Gwencon:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3

        Gwen "Vaya, pensé que podriamos ir a almorzar algo, ya que no nos habiamos visto por mucho..."
        
        Mc "La verdad, no tenia planeado almorzar."

        Gwen "¿Por? [NomUs], debes almorzar algo, sería malo que descuides tus alimentos... Por favor, consideralo."
    
        hide Gwencon

        Mc "Aww, es tierno que te preocupes por mi."

        Gwen "B-Bueno, ¿Quién no lo haría por su amiga?"
           
        Mc "Está bien, agradezco tu consideración. Así que aceptaré tu oferta, me gustaria pasar tiempo contigo."
        show Gwenfeliz:
            xsize 1640
            ysize 1500
            xalign 0.4
            yalign -0.3
         
        Mc "\[Gwen parecia feliz por mi respuesta.\]"
        Mc "(Gwen tomó mi mano, y me llevó a un local.)"
        scene tienda
        Mc "(Ahí pedí algo sencillo, y me senté junto a ella, y comenzamos a charlar mientras almorzabamos.)"
        hide Gwenfeliz
        Mc "(Al finalizar el almuerzo, ambas nos despedimos y cada una fue a lo suyo.)"
        scene depa
        Mc "(Al volver me puse a acomodar un poco mi departamento.\nTambien decidí enviarle mensaje a Gwen, agradeciendole que me haya acompañado el dia de hoy.)"        
        Mc "\[Ella me contestó con un: \"No ha sido nada, disfrute mucho poder encontrarme contigo nuevamente, espero que podamos vernos más seguido. :) \"\]"
        hide Gwenfeliz
        hide Gwen
    return
    return
    #Finaliza el juego
return