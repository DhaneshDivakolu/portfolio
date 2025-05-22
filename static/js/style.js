const a = document.getElementsByTagName("h1");
const dh= document.getElementsByTagName("input");

// for(let i = 0; i < a.length; i++)
// {
//     const d = a[i];
//     d.addEventListener("mouseenter",func())
//     {
//         d.style.boxShadow = "10px 10px 10px red";
//     }
//     d.addEventListener("mouseleave",func())
//     {
//         d.style.boxShadow = "";
//     }
// }

for(let tag=0; tag<dh.length; tag++)
    {
            const ele = dh[tag];
            ele.addEventListener("mouseenter",function(){
                ele.style.fontSize = "40px";
            })
            ele.addEventListener("mouseleave",function(){
                ele.style.fontSize = "";
            })
    }