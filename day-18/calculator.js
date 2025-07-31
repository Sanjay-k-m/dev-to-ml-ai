function calculate(operator) {
  no1 = parseFloat(document.getElementById("no1").value);
  no2 = parseFloat(document.getElementById("no2").value);
  switch (operator) {
    case "+":
      document.getElementById("result").innerText = no1 + no2;
      break;
    case "-":
      document.getElementById("result").innerText = no1 - no2;
      break;
    case "/":
      document.getElementById("result").innerText = no1 / no2;
      break;
    case "%":
      document.getElementById("result").innerText = no1 % no2;
      break;
    case "*":
      document.getElementById("result").innerText = no1 * no2;
      break;
  }
}
