package go.store.inventory.controller;

import go.store.inventory.exception.ResourceNotFoundException;
import go.store.inventory.model.ProductsType;
import go.store.inventory.repository.ProductsTypesRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * The type ProductsType controller.
 *
 * @author Maroun Melhem <https://maroun.me>
 */
@RestController
@RequestMapping("/api/")
public class ProductsTypesController {

  @Autowired
  private ProductsTypesRepository productsTypesRepository;

  /**
   * Get all products-types list.
   *
   * @return the list
   */
  @GetMapping("/products-types")
  public List<ProductsType> getProductsTypes() {
    return productsTypesRepository.findAll();
  }

  /**
   * Gets products Types by id.
   *
   * @param productsTypeId the products Type id
   * @return the products Type by id
   * @throws ResourceNotFoundException the resource not found exception
   */
  @GetMapping("/products-types/{id}")
  public ResponseEntity<ProductsType> getProductsTypeById(@PathVariable(value = "id") Long productsTypeId)
      throws ResourceNotFoundException {
    ProductsType productsType =
            productsTypesRepository
            .findById(productsTypeId)
            .orElseThrow(() -> new ResourceNotFoundException("Products Type not found on :: " + productsTypeId));
    return ResponseEntity.ok().body(productsType);
  }

  /**
   * Create ProductsType productsType.
   *
   * @param productsType productsType
   * @return productsType
   */
  @PostMapping("/products-types")
  public ProductsType createProductsType(@Valid @RequestBody ProductsType productsType) {
    return productsTypesRepository.save(productsType);
  }

  /**
   * Update productsType response entity.
   *
   * @param productsTypeId the productsType id
   * @param productsTypeDetails the productsType details
   * @return the response entity
   * @throws ResourceNotFoundException the resource not found exception
   */
  @PutMapping("/productsTypes/{id}")
  public ResponseEntity<ProductsType> updateProductsType(
      @PathVariable(value = "id") Long productsTypeId, @Valid @RequestBody ProductsType productsTypeDetails)
      throws ResourceNotFoundException {

    ProductsType productsType =
            productsTypesRepository
            .findById(productsTypeId)
            .orElseThrow(() -> new ResourceNotFoundException("ProductsType not found on :: " + productsTypeId));

    productsType.setName(productsTypeDetails.getName());
    productsType.setSlug(productsTypeDetails.getSlug());
    productsType.setUpdatedAt(new Date());
    final ProductsType updatedProductsType = productsTypesRepository.save(productsType);
    return ResponseEntity.ok(updatedProductsType);
  }

  /**
   * Delete productsType map.
   *
   * @param productsTypeId the productsType id
   * @return the map
   * @throws Exception the exception
   */
  @DeleteMapping("/productsType/{id}")
  public Map<String, Boolean> deleteProductsType(@PathVariable(value = "id") Long productsTypeId) throws Exception {
    ProductsType productsType =
            productsTypesRepository
            .findById(productsTypeId)
            .orElseThrow(() -> new ResourceNotFoundException("ProductsType not found on :: " + productsTypeId));

    productsTypesRepository.delete(productsType);
    Map<String, Boolean> response = new HashMap<>();
    response.put("deleted", Boolean.TRUE);
    return response;
  }
}
