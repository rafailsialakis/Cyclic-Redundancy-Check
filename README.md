<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRC Implementation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>CRC Implementation</h1>
        <p>A cyclic redundancy check (CRC) is an error-detecting code commonly used in digital networks and storage devices to detect accidental changes to digital data. Blocks of data entering these systems get a short check value attached, based on the remainder of a polynomial division of their contents. On retrieval, the calculation is repeated and, in the event the check values do not match, corrective action can be taken against data corruption. CRCs can be used for error correction.</p>
        
        <h2>How the Program Works</h2>
        <p>To illustrate how the CRC program works, let's consider an example:</p>
        <ul>
            <li>Let's say the user wants to transmit a message <code>M(x) = 1001100</code>.</li>
            <li>The user selects a polynomial generator. In our case, we select <code>G(x) = x^3 + x^2 + 1</code>.</li>
            <li>The degree of the polynomial is 3, so we append 3 parity bits at the end of our message.</li>
            <li>Now, <code>M(x) = 1001100 000</code>.</li>
            <li>The binary representation of the polynomial is <code>1101</code>.</li>
        </ul>

        <p>This example demonstrates the basic process of using CRC for error detection and correction. The program takes the message and appends parity bits based on a polynomial generator. Upon retrieval, the parity bits are recalculated and compared to ensure data integrity.</p>
        
        <p>Feel free to explore the program further and experiment with different message and polynomial combinations to understand CRC better.</p>
    </div>
</body>
</html>
