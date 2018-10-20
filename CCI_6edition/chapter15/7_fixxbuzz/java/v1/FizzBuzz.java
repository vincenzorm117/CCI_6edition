

public class FizzBuzz extends Thread {

    public enum Type { None, Three, Five, Fifteen }

    public Integer n;
    private static Integer index = 0;
    public Type type;
    private static Object lock = new Object();


    public FizzBuzz(Integer n, Type type) {
        this.n = n;
        this.type = type;
    }

    @Override
    public void run() {
    
        while( true ) {
            synchronized(lock) {
                if( index > n ) {
                    return;
                }
                switch(type) {
                    case Fifteen:
                        if( (index % 15) == 0 ) {
                            System.out.println("FizzBuzz");
                            index += 1;
                        }
                        break;
                    case Three:
                        if( (index % 3) == 0 ) {
                            System.out.println("Fizz");
                            index += 1;
                        }
                        break;
                    case Five:
                        if( (index % 5) == 0 ) {
                            System.out.println("Buzz");
                            index += 1;
                        }
                        break;
                    default:
                        if( (index % 3) != 0 && (index % 5) != 0 ) {
                            System.out.println(index);
                            index += 1;
                        }
                        break;
                }
            }
        }
    }

    public static void main(String[] args) {

        int N = 100;

        FizzBuzz f1 = new FizzBuzz(N, Type.Three);
        FizzBuzz f2 = new FizzBuzz(N, Type.Five);
        FizzBuzz f3 = new FizzBuzz(N, Type.Fifteen);

        f1.start();
        f2.start();
        f3.start();
    }
}