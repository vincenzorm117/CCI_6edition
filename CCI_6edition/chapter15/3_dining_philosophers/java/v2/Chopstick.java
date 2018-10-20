import java.util.concurrent.locks.ReentrantLock;


class Chopstick {
    private ReentrantLock lock;

    public Chopstick() {
        lock = new ReentrantLock();
    }

    public void pickUp() {
        lock.lock();
    }

    public void putDown() {
        lock.unlock();
    }
}