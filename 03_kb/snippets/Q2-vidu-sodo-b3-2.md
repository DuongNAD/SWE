{
  "id": "b3-2",
  "so_do": [
    {
      "ts_day_du_nhat": "29:58",
      "ts_xuat_hien": [
        "26:47",
        "26:49",
        "26:55",
        "27:15",
        "27:21",
        "27:52",
        "28:12",
        "28:20",
        "28:42",
        "29:00",
        "29:08",
        "29:15",
        "29:43",
        "29:52",
        "29:58"
      ],
      "loai": "use_case_diagram",
      "ten_bai_toan": "Integrated Fulfillment System",
      "phan_tu": [
        {
          "ten": "Customers",
          "kieu": "actor"
        },
        {
          "ten": "Delivery Riders",
          "kieu": "actor"
        },
        {
          "ten": "Warehouse Staff",
          "kieu": "actor"
        },
        {
          "ten": "Procurement Team",
          "kieu": "actor"
        },
        {
          "ten": "Managers",
          "kieu": "actor"
        },
        {
          "ten": "Payment Gateway",
          "kieu": "actor"
        },
        {
          "ten": "Mapping Service API",
          "kieu": "actor"
        },
        {
          "ten": "Browse products",
          "kieu": "use_case"
        },
        {
          "ten": "Manage shopping cart",
          "kieu": "use_case"
        },
        {
          "ten": "Checkout",
          "kieu": "use_case"
        },
        {
          "ten": "Retry Payment",
          "kieu": "use_case"
        },
        {
          "ten": "Manage Subscriptio",
          "kieu": "use_case"
        },
        {
          "ten": "Accept orders",
          "kieu": "use_case"
        },
        {
          "ten": "Navigate to customer",
          "kieu": "use_case"
        },
        {
          "ten": "Update status orders",
          "kieu": "use_case"
        },
        {
          "ten": "Update inventory",
          "kieu": "use_case"
        },
        {
          "ten": "Mark item",
          "kieu": "use_case"
        },
        {
          "ten": "UseCase4",
          "kieu": "use_case"
        },
        {
          "ten": "UseCase8",
          "kieu": "use_case"
        },
        {
          "ten": "UseCase11",
          "kieu": "use_case"
        },
        {
          "ten": "UseCase14",
          "kieu": "use_case"
        }
      ],
      "quan_he": [],
      "plantuml": "",
      "ghi_chu": "Sơ đồ vẽ trên StarUML chưa hoàn thiện. Chỉ có các hình nhân vật (actor) và các hình oval (use case), hoàn toàn không có mũi tên/đường nối nào. Một số use case còn chưa được đặt tên (UseCase4, 8, 11, 14). Do không có quan hệ nên không thể xuất mã PlantUML hợp lệ."
    }
  ],
  "bang": [
    {
      "ts": "25:52",
      "tieu_de": "Identify All actors",
      "cot": [
        "Actor",
        "Type",
        "Goal"
      ],
      "dong": [
        [
          "Customers",
          "Primary",
          "Browse products, manage shopping cart, payment,Subscription Mode"
        ],
        [
          "Delivery Riders",
          "Primary",
          "Accept orders, navigate to customer, update status orders"
        ],
        [
          "Warehouse Staff",
          "Primary",
          "inventory management, mark item"
        ],
        [
          "Procurement Team",
          "Secondary",
          "Receive Restock Alert"
        ],
        [
          "Managers",
          "Primary",
          "View sales analytics, managing promotional discount codes and manage refund"
        ],
        [
          "Payment Gateway",
          "Secondary",
          "Handle payment"
        ],
        [
          "Mapping Service API",
          "Secondary",
          "Use map to navigate to customer"
        ]
      ]
    },
    {
      "ts": "39:18",
      "tieu_de": "Danh sách Use Cases",
      "cot": [
        "STT",
        "Use Case",
        "Actor",
        "Description"
      ],
      "dong": [
        [
          "1",
          "Browse products",
          "Customers",
          "View products"
        ],
        [
          "2",
          "Manage shopping cart",
          "Customers",
          "Manage shopping cart"
        ],
        [
          "3",
          "Checkout",
          "Customers",
          "payment"
        ],
        [
          "4",
          "Retry Payment",
          "Customers",
          "If checkout error customer can pay again"
        ],
        [
          "5",
          "Manage Subscription",
          "Customers",
          "customers can schedule recurring weekly deliveries"
        ],
        [
          "6",
          "Accept orders",
          "Delivery Riders",
          "Delivery Riders use a dedicated mobile interface to accept delivery assignments"
        ],
        [
          "7",
          "Navigate to customer",
          "Delivery Riders",
          "navigate to customer locations using integrated maps"
        ],
        [
          "8",
          "Update status orders",
          "Delivery Riders",
          "update the order status to \"Delivered\""
        ],
        [
          "9",
          "Update inventory",
          "Warehouse Staff",
          "responsible for inventory management"
        ],
        [
          "10",
          "Mark item",
          "Warehouse Staff",
          "marking items as \"Damaged\" or \"Out of Stock.\""
        ],
        [
          "11",
          "View sales analytics",
          "Managers",
          "viewing real-time sales analytics"
        ],
        [
          "12",
          "Manage discount code",
          "Managers",
          "managing promotional discount codes"
        ],
        [
          "13",
          "Handle refund request",
          "Managers",
          "Handling customer refund requests for missing items."
        ],
        [
          "14",
          "Receive Restock Alert",
          "Procurement Team",
          "When inventory for a high-demand item falls below a certain threshold, the system automatically triggers a \"Restock Alert\""
        ],
        [
          "15",
          "Process payment",
          "Payment Gateway",
          "the IFS must integrate with a third-party to Process payment"
        ],
        [
          "16",
          "Use map",
          "Mapping Service API",
          "the IFS must integrate with a third-party to Use map"
        ]
      ]
    }
  ],
  "anh_bo_qua": [
    "09m06s.jpg — trình duyệt google",
    "23m56s.jpg — file docs đề bài thuần chữ",
    "29m47s.jpg — task switcher màn hình",
    "30m14s.jpg — task switcher màn hình"
  ]
}