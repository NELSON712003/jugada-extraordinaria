$(document).ready(function(){
    //let videos_json = [{"nombre":"Diego"},{"nombre":"Cazon"}]
    //pinta_datos_video(videos_json)
    console.log("Comienzo!!!")
    all_videos_publicos( pinta_datos_video_usuario )
})

function pinta_datos_video_usuario( json_video ){
    lista_divs_historial.forEach( divs_ingresados => {
        divs_ingresados.remove()
    });
    
    lista_divs_historial = []

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

        $(div_article).find("#cantidad_reproducciones_video_user").text( "Visualizaciones: " + video["cantidad_reproducciones"] )
        $(div_article).find("#fecha_ingreso_video_user").text( "Fecha de Ingreso: " + video["fecha_ingreso"] )
        
        $(div_article).find(".etiqueta_a_url_video").attr( "href" , url_video_single.replace('99999999', String( video["id_video"] ) ) )

        $( div_article ).insertBefore("#div_article_main")
        
        lista_divs_historial.push( div_article )

    });

}

function all_videos_publicos( function_pinta_datos ){
    $.ajax({
        url: api_all_videos_public,
        type:'get',
        data:{
            "limite_inferior":0,
            "limite_superior":15
        },
        dataType:'JSON',
        success: function( request ){
            console.log( request )
            function_pinta_datos( request["all_videos"] )
        },
        error: function( request ){
            console.log("Error 123")
        },
    })
}

function search_video_title(){
    if(event.key === 'Enter') {
        ajax_search_videos( pinta_datos_video_usuario )
    }
}

function ajax_search_videos( function_pinta_datos ){
    
    console.log( $("#input_name_video_serch") )

    let nombre_video_search = $("#input_name_video_serch").val();

    console.log( nombre_video_search )
    $.ajax({
        url: api_search_videos_public,
        type:'get',
        data:{
            "nombre_video_search" : nombre_video_search,
        },
        dataType:'JSON',
        success: function( request ){
            console.log( request )
            function_pinta_datos( request["search_videos"] )
        },
        error: function( request ){
            console.log("Error 123")
        },
    })

}