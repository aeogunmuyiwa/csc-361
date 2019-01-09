## Taking Wireshark for a Test Run

Read the **Wireshark_HTTP_v7.0.pdf** if you need additional help.

  * Start `CSC361-VM`.
  * Start Wireshark with __Capture Filter__ set to `host web.uvic.ca`.
  * Start capture packets from `eth0` (whichever is your default network interface).
  * Open Firefox (or any browser) and clear all its histories and content data.
  * Enter the URL <http://web.uvic.ca/~mcheng/lab1/csc100.html>.
  * After the page loaded, do it again using "reload".
  * Now, you can stop capturing packets in Wireshark but don't close it.
  * After you have completed all the answers, save the Wireshark session into a `.pcap` file.
  * Close Firefox and Wireshark. You are done!

## Questions
Answer the following questions in the space provided. Submit your answers (a modified version of this file) as an attachment to the submission box. (**Note**: You don't need to attach your saved `.pcap` file. But we may ask you to show it in the lab.)


  1. What is the **source IP address** of the HTTP request?
206.87.177.243

  2. What is the **destination IP address** of the HTTP response?
142.104.197.80

  3. What is the **length** of the HTTP response body text in bytes (just the `csc100.html` file,
     not including all other images)?
458 bytes

  4. Which **versions** of HTTP protocol are running on the client and on the server?
HTTP 1.1

  5. What is the **HTTP status code** returned by the server?
  200


  6. When is the **last-modified date** of the requested file `csc100.html`?
Wed, 15 Aug 2018 23:38:03 GMT\r\n

  7. Did you find the HTTP request with `If-Modified-Since:`? What is the packet number? (**Note**: If not, try reload the page.)
NO

  8. Did you see the response status code `304 Not Modified`? What is the packet number? (**Note**: If not, try reload the page.)
NO

  9. In total, how many HTTP GET requests were sent in order to download the whole of `csc100.html` file, including all images?
 5 GET requests

  10. What is the TCP port number used by your browser to download the whole of `csc100.html` file, including all images?
port 60833

  11. Did you find the HTTP request with `If-Modified-Since:`? What is the packet number? (**Note**: If not, try reload the page.) 0250


  12. Did you see the response status code `304 Not Modified`? What is the packet number? (**Note**: Try reload the page.)040