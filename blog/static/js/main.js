var button = document.getElementById("button");

button.addEventListener('click',function(){
    notify();
});

function notify(){
    if (!("Notification" in window)) {
        alert("Tu navegador no soporta notificaciones")
    }else if(Notification.permission === "granted"){
        var notification = new Notification("mi primera notificación");
    }else if(Notification.permission !== "denied"){
        Notification.requestPermission(function(permission){
            if(Notification.permission === "granted"){
                var notification = new Notification("Hola Mundo");
            }
        });
    }

}