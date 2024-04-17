
function user_highlightCurrent( ) {
    const curPage = document.URL ;
    const links = document.getElementsByTagName( "a" ) ;
    for( let link of links ) {
        if( link.href == curPage ) {
            link.classList.add( "active") ;
        }
    }
}

document.addEventListener( "readystatechange" , event => { 
    if( event.target.readyState === "interactive" ) {
        user_highlightCurrent( ) ;
    }
} ) ;

