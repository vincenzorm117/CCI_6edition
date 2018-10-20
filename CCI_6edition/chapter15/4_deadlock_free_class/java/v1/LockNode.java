import java.util.ArrayList;
import java.util.HashMap;
import java.util.concurrent.locks.ReentrantLock;

public class LockNode {
    public enum VisitState { FRESH, VISITING, VISITED };

    private ArrayList<LockNode> children;
    private int lockId;
    private Lock lock;
    private int maxLocks;

    public LockNode(int id, int max) {
        this.lockId = id;
        this.maxLocks = max;
        this.children = new ArrayList<LockNode>();
    }

    public void joinTo(LockNode node) { children.add(node); }
    public remove(LockNode node) { children.remove(node); }

    public boolean hasCycle(HashMap<Integer, Boolean> touchedNodes) {
        VisitState[] visited = new VisitState[maxLocks];
        for(int i = 0; i < maxLocks; i++) {
            visited[i] = VisitState.FRESH;
        }
        return hasCycle(visited, touchedNodes);
    }

    private boolean hasCycle(VisitState[] visited, HashMap<Integer, Boolean> touchedNodes) {
        if(touchedNodes.containsKey(lockId)) {
            touchedNodes.put(lockId, true);
        }

        if(visited[lockId] == VisitState.VISITING) {
            return true;
        } else if( visited[lockId] == VisitState.FRESH) {
            visited[lockId] = VisitState.VISITING;
            for(LockNode n : children) {
                if( n.hasCycle(visited, touchedNodes) ) {
                    return true;
                }
            }
            visited[lockId] = VisitState.VISITED;
        }
        return false;
    }

    public Lock getLock() {
        if( lock == null ) lock = new ReentrantLock();
        return lock;
    }

    public int getId() { return lockId; }
}