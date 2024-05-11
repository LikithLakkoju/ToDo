const editbtns=document.querySelectorAll('#editbtn')
editbtns.forEach(editbtn =>{
    editbtn.addEventListener('click', function(){
        const id=editbtn.getAttribute("databtn")
        console.log(id)
        
        editbtn.innerHTML= editbtn.innerHTML=='Edit'?'Save':'Edit'
        const todo=document.getElementById(`todo-${id}`)
        todo.style.border=todo.style.border=='none'?'1px solid black':'none'
        let todostatus=todo.getAttribute("contenteditable")
        todostatus=todostatus=='true'?false:true

        todo.setAttribute("contenteditable",todostatus);
        const update=document.getElementById(`update-${id}`)
        update.setAttribute("href",`/update?id=${id}&value=${todo.innerHTML}`)

    })
})