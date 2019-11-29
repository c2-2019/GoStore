package GoAuth.service;

import GoAuth.entity.Cart;
import GoAuth.entity.ProductInOrder;
import GoAuth.entity.User;

import java.util.Collection;

/**
 * Created By Peter.
 */
public interface CartService {
    Cart getCart(User user);

    void mergeLocalCart(Collection<ProductInOrder> productInOrders, User user);

    void delete(String itemId, User user);

    void checkout(User user);
}
