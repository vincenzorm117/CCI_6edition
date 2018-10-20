import java.util.concurrent.locks.ReentrantLock;


class Chopstick {
    private ReentrantLock lock;
    private int id;

    public Chopstick(int id) {
        lock = new ReentrantLock();
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public void pickUp() {
        lock.lock();
    }

    public void putDown() {
        lock.unlock();
    }
}