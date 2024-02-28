import { Product } from "./products";

export interface Categories{
    id: number,
    name: string;
    products: number[],
    show_products: boolean;
}

export const categories = [
    {
        id: 1,
        name: 'Watches',
        products: [1, 2],
        show_products: false
    },

    {
        id: 2, 
        name: 'Phones', 
        products: [3, 10
        ], 
        show_products: false
    },

    {
        id: 3,
        name: 'Keyboards', 
        products: [6, 7, 5
        ]
    }, 

    {
        id: 4,
        name: 'Others', 
        products: [9, 8, 5, 4
        ],
        show_products: false
    }
];
