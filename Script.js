onload=init;

function init(){
      document
       .queryselector("button")
       .addEventLisner(
         "click",
          onClick,
          false
          );
}
   function onClick(){
      document.body
       .classList
       .toggle("style-gordan");
}
