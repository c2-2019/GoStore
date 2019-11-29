package GoAuth.service;

import GoAuth.entity.ProductCategory;

import java.util.List;

/**
 * Created By louay ayoub.
 */
public interface CategoryService {

    List<ProductCategory> findAll();

    ProductCategory findByCategoryType(Integer categoryType);

    List<ProductCategory> findByCategoryTypeIn(List<Integer> categoryTypeList);

    ProductCategory save(ProductCategory productCategory);


}
