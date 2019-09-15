package go.store.inventory.repository;

import go.store.inventory.model.ProductsType;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * The interface ProductsTypes repository.
 *
 * @author Maroun Melhem <https://maroun.me>
 */
@Repository
public interface ProductsTypesRepository extends JpaRepository<ProductsType, Long> {}
