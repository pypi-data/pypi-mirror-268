def javaslip():
    print("""public class S1Q1 extends Thread 
          { 
            public void run() 
            { 
                try 
                { 
                    for(char c = 'A'; c <= 'Z'; c++) 
                    { 
                        System.out.println("Generated Charachter: " + c);
                        Thread.sleep(2000); 
                    } 
                } 
                catch(InterruptedException e) 
                { 
                    System.out.println(e); 
                } 
            } 
            public static void main(String args[]) 
            { 
                S1Q1 t1 = new S1Q1(); 
                t1.start(); 
            } 
        }""")
   