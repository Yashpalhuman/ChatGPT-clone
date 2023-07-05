async function postData(url = "", data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: "POST", headers: {
        "Content-Type": "application/json",
      },  body: JSON.stringify(data), 
    });
    return response.json(); 
  }
  



var sendbutton=document.getElementById("sendButton");
var sendbutton2=document.getElementById("sendButton2");

sendbutton.addEventListener("click",async()=>{
    // alert("hello");
     question=document.getElementById("question").value;
     document.getElementById("question").value="";
     document.querySelector(".right2").style.display="block";
     document.querySelector(".right1").style.display="none";

     document.getElementById("question2").innerHTML=question;

     let result= await postData("/api",{"question":question})
     solution.innerHTML=result.answer
})
// sendbutton2.addEventListener("click",()=>{
//     // alert("hello");
//      question1=document.getElementById("question1").value;
//      document.getElementById("question1").value="";
//      document.querySelector(".right2").style.display="block";
//      document.querySelector(".right1").style.display="none";

//      document.getElementById("question2").innerHTML=question1;
// })

