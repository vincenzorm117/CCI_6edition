import java.util.ArrayList;

class Philosopher extends Thread {

    private int bites = 10;
    private Chopstick left, right;
    public int id;

    public Philosopher(int id, Chopstick left, Chopstick right) {
        this.id = id;
        
        if( left.getId() < right.getId() ) {
            this.left = left;
            this.right = right;
        } else {
            this.left = right;
            this.right = left;
        }
    }

    public void eat() {
        pickUp();
        chew();
        putDown();
    }

    public void pickUp() {
        left.pickUp();
        right.pickUp();
    }

    public void chew() {
        System.out.printf("Philosopher[%d] chewing.\n\r", this.id);
    }

    public void putDown() {
        right.putDown();
        left.putDown();
    }

    public void run() {
        for(int i = 0; i < bites; i++) {
            this.eat();
        }
    }

    public static void main(String[] args) {
        Chopstick[] chopsticks = new Chopstick[20];
        Philosopher[] philosophers = new Philosopher[20];
        
        for(int i = 0; i < chopsticks.length; i++) {
            chopsticks[i] = new Chopstick(i);
        }

        for(int i = 0; i < philosophers.length; i++) {
            philosophers[i] = new Philosopher(i, chopsticks[i], chopsticks[(i+1)%20]);
        }

        for(int i = 0; i < philosophers.length; i++) {
            philosophers[i].start();
        }
        
    }
}