import java.io.*;
import java.net.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

public class Server {
    private static final int MAX_CLIENTS = 5;
    private static final AtomicInteger clientCounter = new AtomicInteger(0);
    private static final ExecutorService threadPool = Executors.newFixedThreadPool(MAX_CLIENTS);

    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(1234);
        System.out.println("Server started, waiting for connections...");

        while (true) {
            Socket clientSocket = serverSocket.accept();
            if (clientCounter.get() < MAX_CLIENTS) {
                threadPool.execute(new ClientHandler(clientSocket, clientCounter));
            } else {
                System.out.println("Maximum client limit reached. Rejecting new connection.");
                // Optionally, send a message to the client indicating that the server is full.
                // We can do this before closing the socket.
                try (PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {
                    out.println("Server is currently full. Please try again later.");
                } catch (IOException e) {
                    e.printStackTrace();
                }
                clientSocket.close();
            }
        }
    }
}

class ClientHandler implements Runnable {
    private Socket clientSocket;
    private int clientId;
    private AtomicInteger clientCounter;

    public ClientHandler(Socket socket, AtomicInteger counter) {
        this.clientSocket = socket;
        this.clientId = counter.incrementAndGet(); // Increment and get the new value
        this.clientCounter = counter;
    }

    public void run() {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
             PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

            // Display client's address and port
            String clientAddress = clientSocket.getInetAddress().getHostAddress();
            int clientPort = clientSocket.getPort();
            System.out.println("Client-" + clientId + " connected from " + clientAddress + ":" + clientPort);

            String clientName = "Client-" + clientId;

            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                // Process the input and send response
                // Include client's address and port in the message sent to the server
                String messageToSend = clientName + " [" + clientAddress + ":" + clientPort + "]: " + inputLine;
                out.println(messageToSend);
            }
        } catch (IOException e) {
            System.out.println("Exception caught when trying to listen on port or listening for a connection");
            System.out.println(e.getMessage());
            e.printStackTrace();
        } finally {
            System.out.println("Client disconnected: " + clientId);
            clientCounter.decrementAndGet();
            try {
                clientSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
