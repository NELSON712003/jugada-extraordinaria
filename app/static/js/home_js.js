$(document).ready(function(){
    //let videos_json = [{"nombre":"Diego"},{"nombre":"Cazon"}]
    //pinta_datos_video(videos_json)
    console.log("Comienzo!!!")
    obtener_info_videos( pinta_datos_video_usuario )
    obtiene_infor_top_videos( pinta_datos_top_videos_publicos )
    console.log("Final!!!")
    var url_raiz = window.location.href.substring(0, 22) //Raiz donde se encuentra la raiz de la app
    console.log( "Url Raiz: " + url_raiz )
})

function pinta_datos_video_usuario( json_video ){
    json_video.forEach( video => {
        let div_article = $("#div_article_main").clone()
        $(div_article).attr("hidden",false)

        $(div_article).find("#titulo_video").text( video["titulo"] )
        $(div_article).find(".published").text( video["fecha_ingreso"] )
        $(div_article).find(".author").text( video["username"] )
        
        $(div_article).find("#image_video").attr("src",  video["imagen"].replace('/app','') ) //Quitamos /app de la url
        //$(div_article).find("#image_video").attr("width",  '500' )
        $(div_article).find("#image_video").css( "maxWidth", "65%" )
        //$(div_article).find("#image_video").css( "maxHeight", "350" )
        //$(div_article).find("#image_video").attr("height",  '550' )

        $(div_article).find("#cantidad_reproducciones_video_user").text( video["cantidad_reproducciones"] + "visualizaciones" )
        $(div_article).find("#fecha_ingreso_video_user").text( "Fecha de Ingreso: " + video["fecha_ingreso"] )
        
        $(div_article).find(".etiqueta_a_url_video").attr( "href" , url_video_single.replace('99999999', String( video["id_video"] ) ) )

        $( div_article ).insertBefore("#div_article_main")
    }); 
}

function pinta_datos_top_videos_publicos( json_video ){
    const json_video_reverse = json_video.reverse();
    json_video_reverse.forEach( video => {
        let div_mini_article = $("#div_article_section").clone()
        $(div_mini_article).attr("hidden",false)

        $(div_mini_article).find("h3").text( video["titulo"] )
        $(div_mini_article).find(".author").text( video["username"] )
        $(div_mini_article).find("#cantidad_reproducciones").text( "Reproducciones: " + video["cantidad_reproducciones"] )
        $(div_mini_article).find("#fecha_publicasion").text( "Fecha: " + video["fecha_ingreso"] )
        
        $(div_mini_article).find("#image_video").attr("src", video["imagen"].replace('/app','') )
        $(div_mini_article).find("#image_video").css( "maxWidth", "85%" )

        $(div_mini_article).find(".etiqueta_a_url_video").attr( "href" , url_video_single.replace('99999999', String( video["id_video"] ) ) )

        $( div_mini_article ).insertBefore("#div_article_section")
    }); 
}

function obtener_info_videos( function_pinta_datos ){
    $.ajax({
        url:'/app/api_videos/',
        type:'get',
        data:{
            "limite_inferior":0,
            "limite_superior":10
        },
        dataType:'JSON',
        success: function( request ){
            console.log( request )
            function_pinta_datos( request["videos_user"] )
        },
        error: function( request ){
            console.log("Error 123")
        },
    })
}

function obtiene_infor_top_videos( function_pinta_datos ){
    $.ajax({
        url:'/app/api_top_videos/',
        type:'get',
        data:{
            "limite_inferior":0,
            "limite_superior":5
        },
        dataType:'JSON',
        success: function( request ){
            console.log( request )
            function_pinta_datos( request["top_videos"] )
        },
        error: function( request ){
            console.log("Error 123")
        },
    })
}