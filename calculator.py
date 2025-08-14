<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Animated Calculator</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
        }
        
        .calculator {
            width: 380px;
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
            overflow: hidden;
            transform: translateY(30px);
            opacity: 0;
            animation: fadeInUp 0.6s ease-out forwards;
        }
        
        @keyframes fadeInUp {
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }
        
        .display {
            width: 100%;
            height: 100px;
            font-size: 36px;
            text-align: right;
            padding: 0 20px;
            border: none;
            background-color: #f8f9fa;
            color: #333;
            box-sizing: border-box;
            outline: none;
            font-weight: 300;
            letter-spacing: 1px;
            transition: all 0.3s ease;
        }
        
        .display:focus {
            background-color: #e9ecef;
        }
        
        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-gap: 1px;
            background-color: #ddd;
        }
        
        button {
            height: 80px;
            font-size: 24px;
            border: none;
            background-color: #fff;
            cursor: pointer;
            transition: all 0.2s ease;
            position: relative;
            overflow: hidden;
            font-weight: 500;
            color: #333;
        }
        
        button:before {
            content: "";
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.7);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }
        
        button:hover {
            background-color: #f2f2f2;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        button:active {
            transform: translateY(0);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        button:active:before {
            width: 300px;
            height: 300px;
        }
        
        .clear {
            grid-column: span 4;
            background-color: #ff6b6b;
            color: white;
            font-weight: bold;
            height: 70px;
        }
        
        .clear:hover {
            background-color: #ff5252;
        }
        
        .equals {
            background-color: #4CAF50;
            color: white;
        }
        
        .equals:hover {
            background-color: #45a049;
        }
        
        .operator {
            background-color: #f0f0f0;
            color: #ff9800;
        }
        
        .operator:hover {
            background-color: #e0e0e0;
        }
        
        .digit {
            animation: popIn 0.3s ease-out;
        }
        
        @keyframes popIn {
            0% {
                transform: scale(0.8);
                opacity: 0;
            }
            50% {
                transform: scale(1.05);
            }
            100% {
                transform: scale(1);
                opacity: 1;
            }
        }
        
        .display-value {
            animation: slideIn 0.3s ease-out;
        }
        
        @keyframes slideIn {
            from {
                transform: translateX(20px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        .error {
            animation: shake 0.5s ease-in-out;
            color: #ff6b6b !important;
        }
        
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
            20%, 40%, 60%, 80% { transform: translateX(5px); }
        }
        
        .calculator-title {
            text-align: center;
            padding: 15px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            color: white;
            font-size: 24px;
            font-weight: 600;
            letter-spacing: 1px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <div class="calculator">
        <div class="calculator-title">CALCULATOR</div>
        <input type="text" class="display" readonly>
        <div class="buttons">
            <button class="digit">7</button>
            <button class="digit">8</button>
            <button class="digit">9</button>
            <button class="operator">/</button>
            <button class="digit">4</button>
            <button class="digit">5</button>
            <button class="digit">6</button>
            <button class="operator">*</button>
            <button class="digit">1</button>
            <button class="digit">2</button>
            <button class="digit">3</button>
            <button class="operator">-</button>
            <button class="digit">0</button>
            <button class="digit">.</button>
            <button class="equals">=</button>
            <button class="operator">+</button>
            <button class="clear">C</button>
        </div>
    </div>

    <script>
        const display = document.querySelector('.display');
        const buttons = document.querySelectorAll('button');
        
        // Add animation class to buttons on page load
        buttons.forEach((button, index) => {
            setTimeout(() => {
                button.classList.add('digit');
            }, index * 50);
        });
        
        buttons.forEach(button => {
            button.addEventListener('click', () => {
                const value = button.textContent;
                
                // Add ripple effect
                const ripple = document.createElement('span');
                ripple.classList.add('ripple');
                button.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
                
                if (value === 'C') {
                    display.value = '';
                    display.classList.remove('error');
                } else if (value === '=') {
                    try {
                        // Add animation before calculation
                        display.classList.add('display-value');
                        
                        const result = eval(display.value);
                        display.value = result;
                        
                        // Remove animation class after animation completes
                        setTimeout(() => {
                            display.classList.remove('display-value');
                        }, 300);
                    } catch (error) {
                        display.value = 'Error';
                        display.classList.add('error');
                        
                        // Remove error class after animation
                        setTimeout(() => {
                            display.classList.remove('error');
                        }, 500);
                    }
                } else {
                    display.value += value;
                    
                    // Add animation when adding digits
                    if (!isNaN(value) || value === '.') {
                        display.classList.add('display-value');
                        
                        // Remove animation class after animation completes
                        setTimeout(() => {
                            display.classList.remove('display-value');
                        }, 300);
                    }
                }
            });
        });
        
        // Add keyboard support
        document.addEventListener('keydown', (e) => {
            const key = e.key;
            
            if (key >= '0' && key <= '9' || key === '.' || 
                key === '+' || key === '-' || key === '*' || key === '/') {
                display.value += key;
                display.classList.add('display-value');
                setTimeout(() => {
                    display.classList.remove('display-value');
                }, 300);
            } else if (key === 'Enter' || key === '=') {
                try {
                    display.classList.add('display-value');
                    const result = eval(display.value);
                    display.value = result;
                    setTimeout(() => {
                        display.classList.remove('display-value');
                    }, 300);
                } catch (error) {
                    display.value = 'Error';
                    display.classList.add('error');
                    setTimeout(() => {
                        display.classList.remove('error');
                    }, 500);
                }
            } else if (key === 'Escape' || key === 'c' || key === 'C') {
                display.value = '';
                display.classList.remove('error');
            }
        });
    </script>
</body>
</html>
