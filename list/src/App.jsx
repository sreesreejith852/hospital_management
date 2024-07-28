import {useState} from "react"
import { NewTodoForm } from "./NewTodoForm"
import "./style.css"
import { TodoList } from "./TodoList"


export default function APP(){

  const [todos,setTodos] = useState([])

  function addTodo(title){
    setTodos(currentTodos => {
      return [
        ...currentTodos,
        {id:crypto.randomUUID(),title,completed:false},
      ]
    })
  }

  function toggleTodo(id,completed){
    setTodos(currentTodos => {
      return currentTodos.map(todo => {
        if(todo.id === id){
          todo.completed = completed
          return {...todo,completed}
        }
        return todo
      })
    })
  }
  function deleteTodo(id){
    console.log("sfjshdjasdasdhklfhldfnh")
    setTodos(currentTodos => {
      return currentTodos.filter(todo => todo.id !==id)
    })
  }
  return(

    <>
      <NewTodoForm onSubmit={addTodo}/>       
      <h1 className="header">Todo list</h1>
      <TodoList todos={todos} toggleTodo={toggleTodo} deleteTodo={deleteTodo}/>
    </> 
  )


}
