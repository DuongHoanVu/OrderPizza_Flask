var order = {
  customer : {
    first_name : "",
    last_name : ""
  },
  pizza : [
    {
      pizza_type : "Select pizza type",
      pizza_size : "Select pizza size",
      pizza_count: 'Select pizza number',
    },
    {
      pizza_type : "Select pizza type",
      pizza_size : "Select pizza size",
      pizza_count: 'Select pizza number',
    }
  ]
}

function render_view(order) {
  document.getElementById("confirmation").innerHTML = "Customer name: " +
    order.customer.first_name + " " + order.customer.last_name

  ordersTable = document.getElementById("ordersTable")
  tableBody = ordersTable.getElementsByTagName("tbody")[0]

  tableBody.innerHTML = ""

  var row = tableBody.insertRow(0)

  var cell1 = row.insertCell(0)
  cell1.innerHTML = order.pizza[0].pizza_type
  var cell2 = row.insertCell(1)
  cell2.innerHTML = order.pizza[0].pizza_size
  var cell3 = row.insertCell(2)
  cell3.innerHTML = order.pizza[0].pizza_count

  var row = tableBody.insertRow(1)
  var cell1 = row.insertCell(0)
  cell1.innerHTML = order.pizza[1].pizza_type
  var cell2 = row.insertCell(1)
  cell2.innerHTML = order.pizza[1].pizza_size
  var cell3 = row.insertCell(2)
  cell3.innerHTML = order.pizza[1].pizza_count

  document.getElementById("rawJson").innerHTML = "<pre>" + JSON.stringify(order, null, " ") + "</pre>"
}

render_view(order)

function createOrder() {
    var firstName = document.getElementById("firstNameInput").value
    var lastName = document.getElementById("lastNameInput").value
    
    var pizzaType1 = document.querySelector('input[name="pizzaType1"]:checked').value
    var pizzaSize1 = document.querySelector('input[name="pizzaSize1"]:checked').value
    var pizzaCount1 = document.querySelector('input[name="pizzaCount1"]').value
    
    var pizzaType2 = document.querySelector('input[name="pizzaType2"]:checked').value
    var pizzaSize2 = document.querySelector('input[name="pizzaSize2"]:checked').value
    var pizzaCount2 = document.querySelector('input[name="pizzaCount2"]').value

    order.customer.first_name = firstName
    order.customer.last_name = lastName
    
    order.pizza[0].pizza_type = pizzaType1
    order.pizza[0].pizza_size = pizzaSize1
    order.pizza[0].pizza_count = pizzaCount1

    order.pizza[1].pizza_type = pizzaType2
    order.pizza[1].pizza_size = pizzaSize2
    order.pizza[1].pizza_count = pizzaCount2

    render_view(order)
}

document.querySelector("#addToCartButton").addEventListener("click", createOrder)
