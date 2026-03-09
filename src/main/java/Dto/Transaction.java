package Dto;

import java.sql.Timestamp;

public class Transaction {
//    {'transactionID': '4ce4a330-7043-485b-85be-57368318d39e', 'productID': 'product3',
//    'productName': 'watch', 'productCategory': 'fashion', 'productPrice': 285.87,
//    'productQuantity': 5, 'productBrand': 'mi', 'currency': 'USD', 'customerID': 'fuentesjoshua',
//    'transactionDate': '2026-03-09T07:13:06.2026-03-09','paymentMethod': 'debitCard', 'totalAmount': 1429.35}
    private String transactionID;
    private String productID;
    private String productName;
    private String productCategory;
    private double productPrice;
    private int productQuantity;
    private String productBrand;
    private double totalAmount;
    private String currency;
    private String customerId;
    private Timestamp transactionDate;
    private String paymentMethod;

}
