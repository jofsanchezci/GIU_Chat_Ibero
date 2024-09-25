let currentInput = '0';
let operator = null;
let previousInput = '';
let shouldResetDisplay = false;

// Actualiza la pantalla de la calculadora
function updateDisplay() {
    const display = document.getElementById('display');
    display.innerText = currentInput;
}

// Función para ingresar números
function inputNumber(num) {
    if (shouldResetDisplay) {
        currentInput = num;
        shouldResetDisplay = false;
    } else {
        currentInput = currentInput === '0' ? num : currentInput + num;
    }
    updateDisplay();
}

// Función para ingresar operadores (+, -, *, /)
function inputOperator(op) {
    if (operator !== null) calculate();
    previousInput = currentInput;
    operator = op;
    shouldResetDisplay = true;
}

// Función para ingresar un decimal
function inputDecimal() {
    if (!currentInput.includes('.')) {
        currentInput += '.';
    }
    updateDisplay();
}

// Función para cambiar el signo (+/-)
function toggleSign() {
    currentInput = currentInput.charAt(0) === '-' ? currentInput.slice(1) : '-' + currentInput;
    updateDisplay();
}

// Función para borrar todo (AC)
function clearAll() {
    currentInput = '0';
    operator = null;
    previousInput = '';
    shouldResetDisplay = false;
    updateDisplay();
}

// Función para realizar el cálculo (=)
function calculate() {
    if (operator === null) return;
    let result;
    const prev = parseFloat(previousInput);
    const curr = parseFloat(currentInput);
    
    switch (operator) {
        case '+':
            result = prev + curr;
            break;
        case '-':
            result = prev - curr;
            break;
        case '*':
            result = prev * curr;
            break;
        case '/':
            result = prev / curr;
            break;
        case '%':
            result = prev % curr;
            break;
        default:
            return;
    }
    currentInput = result.toString();
    operator = null;
    shouldResetDisplay = true;
    updateDisplay();
}
