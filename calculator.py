<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Small Colorful Calculator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-image: url('https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            position: relative;
            overflow: hidden;
        }
        
        body::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(76, 175, 80, 0.7), rgba(33, 150, 243, 0.7), rgba(156, 39, 176, 0.7));
            z-index: -1;
            animation: colorShift 15s ease infinite;
        }
        
        @keyframes colorShift {
            0% { background: linear-gradient(135deg, rgba(76, 175, 80, 0.7), rgba(33, 150, 243, 0.7), rgba(156, 39, 176, 0.7)); }
            25% { background: linear-gradient(135deg, rgba(255, 193, 7, 0.7), rgba(244, 67, 54, 0.7), rgba(233, 30, 99, 0.7)); }
            50% { background: linear-gradient(135deg, rgba(0, 188, 212, 0.7), rgba(139, 195, 74, 0.7), rgba(255, 152, 0, 0.7)); }
            75% { background: linear-gradient(135deg, rgba(103, 58, 183, 0.7), rgba(233, 30, 99, 0.7), rgba(0, 150, 136, 0.7)); }
            100% { background: linear-gradient(135deg, rgba(76, 175, 80, 0.7), rgba(33, 150, 243, 0.7), rgba(156, 39, 176, 0.7)); }
        }
        
        .calculator-container {
            width: 100%;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .calculator {
            width: 320px; /* Reduced from 90% max-width 500px */
            background-color: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(15px);
            border-radius: 20px; /* Reduced from 30px */
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4); /* Reduced shadow */
            overflow: hidden;
            transform: scale(0.8);
            opacity: 0;
            animation: scaleIn 0.6s ease-out forwards;
            border: 2px solid rgba(255, 255, 255, 0.5);
        }
        
        @keyframes scaleIn {
            to {
                transform: scale(1);
                opacity: 1;
            }
        }
        
        .display {
            width: 100%;
            height: 70px; /* Reduced from 120px */
            font-size: 32px; /* Reduced from 48px */
            text-align: right;
            padding: 0 20px; /* Reduced from 30px */
            border: none;
            background-color: rgba(248, 249, 250, 0.8);
            color: #333;
            box-sizing: border-box;
            outline: none;
            font-weight: 300;
            letter-spacing: 1px; /* Reduced from 2px */
            transition: all 0.3s ease;
            backdrop-filter: blur(5px);
        }
        
        .display:focus {
            background-color: rgba(233, 236, 239, 0.9);
        }
        
        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-gap: 1px; /* Reduced from 2px */
            background-color: rgba(221, 221, 221, 0.5);
        }
        
        button {
            height: 60px; /* Reduced from 100px */
            font-size: 24px; /* Reduced from 32px */
            border: none;
            background-color: rgba(255, 255, 255, 0.9);
            cursor: pointer;
            transition: all 0.2s ease;
            position: relative;
            overflow: hidden;
            font-weight: 600;
            color: #333;
            backdrop-filter: blur(5px);
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
            transform: translateY(-2px); /* Reduced from 3px */
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1); /* Reduced shadow */
        }
        
        button:active {
            transform: translateY(0);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        button:active:before {
            width: 200px; /* Reduced from 400px */
            height: 200px; /* Reduced from 400px */
        }
        
        .clear {
            grid-column: span 4;
            background: linear-gradient(90deg, #ff6b6b, #ff5252);
            color: white;
            font-weight: bold;
            height: 50px; /* Reduced from 90px */
            font-size: 24px; /* Reduced from 36px */
        }
        
        .clear:hover {
            background: linear-gradient(90deg, #ff5252, #ff1744);
        }
        
        .equals {
            background: linear-gradient(90deg, #4CAF50, #45a049);
            color: white;
        }
        
        .equals:hover {
            background: linear-gradient(90deg, #45a049, #388E3C);
        }
        
        .operator {
            background: linear-gradient(90deg, #FF9800, #F57C00);
            color: white;
        }
        
        .operator:hover {
            background: linear-gradient(90deg, #F57C00, #E65100);
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
                transform: translateX(20px); /* Reduced from 30px */
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
            10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); } /* Reduced from 8px */
            20%, 40%, 60%, 80% { transform: translateX(5px); } /* Reduced from 8px */
        }
        
        .calculator-title {
            text-align: center;
            padding: 15px; /* Reduced from 20px */
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #f5576c);
            background-size: 300% 300%;
            color: white;
            font-size: 24px; /* Reduced from 32px */
            font-weight: 700;
            letter-spacing: 1px; /* Reduced from 2px */
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            backdrop-filter: blur(5px);
            animation: gradientShift 8s ease infinite;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .background-credit {
            position: absolute;
            bottom: 15px;
            right: 15px;
            color: rgba(255, 255, 255, 0.8);
            font-size: 14px;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.7);
            z-index: 1;
            background-color: rgba(0, 0, 0, 0.3);
            padding: 5px 10px;
            border-radius: 15px;
        }
        
        .background-credit a {
            color: rgba(255, 255, 255, 0.9);
            text-decoration: none;
            font-weight: 500;
        }
        
        .background-credit a:hover {
            text-decoration: underline;
        }
        
        @media (max-width: 768px) {
            .calculator {
                width: 280px; /* Reduced from 320px */
                border-radius: 15px;
            }
            
            .display {
                height: 60px; /* Reduced from 70px */
                font-size: 28px; /* Reduced from 32px */
            }
            
            button {
                height: 50px; /* Reduced from 60px */
                font-size: 20px; /* Reduced from 24px */
            }
            
            .calculator-title {
                font-size: 20px; /* Reduced from 24px */
                padding: 12px; /* Reduced from 15px */
            }
            
            .clear {
                height: 45px; /* Reduced from 50px */
                font-size: 20px; /* Reduced from 24px */
            }
        }
        
        @media (max-width: 480px) {
            .calculator {
                width: 260px; /* Reduced from 280px */
                border-radius: 12px;
            }
            
            .display {
                height: 50px; /* Reduced from 60px */
                font-size: 24px; /* Reduced from 28px */
            }
            
            button {
                height: 45px; /* Reduced from 50px */
                font-size: 18px; /* Reduced from 20px */
            }
            
            .calculator-title {
                font-size: 18px; /* Reduced from 20px */
                padding: 10px; /* Reduced from 12px */
            }
            
            .clear {
                height: 40px; /* Reduced from 45px */
                font-size: 18px; /* Reduced from 20px */
            }
        }
    </style>
</head>
<body>
    <div class="calculator-container">
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
    </div>
    
    <div class="background-credit">
        Photo by <a href="https://unsplash.com/@davidmarcu" target="_blank">David Marcu</a> on <a href="https://unsplash.com" target="_blank">Unsplash</a>
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
