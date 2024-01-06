<h1>CRC Implementation:</h1>
<h5>A cyclic redundancy check (CRC) is an error-detecting code commonly used in digital networks and storage devices to detect accidental changes to digital data. Blocks of data entering these systems get a short check value attached, based on the remainder of a polynomial division of their contents. On retrieval, the calculation is repeated and, in the event the check values do not match, corrective action can be taken against data corruption. CRCs can be used for error correction </h5>
<h2>How the program works:</h2>
<h5>Let's say the user wants to transmit a message M(x) = 1001100. He has to select a polynomial generator. In our case we select G(x) = x^3 + x^2 + 1. The degree of the polynomial is 3, so we append 3 parity bits at the end of our message. Now M(x) = 1001100 000. The binary representation of the polynomial is 1101.</h5>
<h1>CRC</h1>
<pre><h5>
Message Transmitter                                                Message Receiver
1001100000                                                         1001100001
1101                                                               1101
 1001                                                               1001
 1101                                                               1101
  1010                                                               1000
  1101                                                               1101
   1110                                                               1010
   1101                                                               1101
     1100                                                              1110
     1101                                                              1101
      001                                                                1101 
                                                                         1101
                                                                         0000
</h5></pre>                                                                
<h5>  100011</h5>
