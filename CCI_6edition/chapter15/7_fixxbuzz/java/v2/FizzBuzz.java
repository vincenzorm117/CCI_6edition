




public class FizzBuzz extends Thread {

    private boolean div3;
    private boolean div5;
    String message;
    private static Object lock = new Object();
    protected static int current = 1;
    private int max;

    public FizzBuzz(boolean div3, boolean div5, int max, String message) {
        this.div3 = div3;
        this.div5 = div5;
        this.message = message;
        this.max = max;
    }

    public void print() {
        System.out.printf(message, current);
        System.out.println();
    }

    @Override
    public void run() {
        while(true) {
            synchronized(lock) {
                if( current > max ) return;

                if( (current % 3 == 0) == div3 && (current % 5 == 0) == div5 ) {
                    print();
                    current++;
                }
            }
        }
    }

    public static void main(String[] args) {
        
        int max = 100;

        Thread[] threads = {
            new FizzBuzz(false, false, max, "%d"),
            new FizzBuzz(false, true, max, "Buzz"),
            new FizzBuzz(true, false, max, "Fizz"),
            new FizzBuzz(true, true, max, "FizzBuzz")
        };

        for(Thread thread : threads) {
            thread.start();
        }
    }
}