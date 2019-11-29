package GoAuth.repository;

import GoAuth.entity.Cart;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Created By louay ayoub.
 */

public interface CartRepository extends JpaRepository<Cart, Integer> {
}
