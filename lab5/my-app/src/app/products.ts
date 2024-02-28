export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  rating: number;
  img: string[];
  link: string;
  show: boolean;

}

export const products = [
  {
    id: 1,
    name: 'Apple Watch SE 40',
    price: 131324,
    description: 'Watch!',
    rating: 5,
    img: [
      'https://resources.cdn-kaspi.kz/img/m/p/h52/h62/63868241969182.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/ha3/h60/63868199403550.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/hd9/h47/63868238200862.jpg?format=gallery-medium'
    ],
    link: 'https://kaspi.kz/shop/p/apple-watch-se-40-mm-chernyi-100568123/?c=750000000',
    show: true,
  },

  {
    id: 2,
    name: 'Xiaomi Smart Band 8 Global Version ',
    price: 17383,
    description: 'Top',
    rating: 5,
    img: [
      'https://resources.cdn-kaspi.kz/img/m/p/h05/h87/83701583446046.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h14/h8a/83701585608734.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/hd9/h47/63868238200862.jpg?format=gallery-medium'
    ],
    link: 'https://kaspi.kz/shop/p/xiaomi-smart-band-8-global-version-chernyi-113260965/?c=750000000',
    show: true,
  },

  {
    id: 3,
    name: 'Xiaomi Redmi 12',
    price: 73252,
    description: 'Xiaomi',
    rating: 5,
    img: [
      'https://resources.cdn-kaspi.kz/img/m/p/h75/hbc/81335343775774.png?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h25/h7e/81335344136222.png?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h3a/hac/81335343939614.jpg?format=gallery-medium'
    ],
    link: 'https://kaspi.kz/shop/p/xiaomi-redmi-12-4g-8-gb-256-gb-chernyi-110918152/?c=750000000',
    show: true,
  },

  {
    id: 4,
    name: 'Apple MacBook Air 15',
    price: 602999,
    description: 'Lol Macbook',
    rating: 5,
    img: [
      'https://resources.cdn-kaspi.kz/img/m/p/h65/h41/81547557240862.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/ha3/h60/63868199403550.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h1c/hd3/81547557371934.jpg?format=gallery-medium'
    ],
    link: 'https://kaspi.kz/shop/p/apple-macbook-air-15-2023-mqkw3-sinii-111217728/?c=750000000',
    show: true,
  },

  {
    id: 5,
    name: 'Spider-Man 2 PS5',
    price: 27500,
    description: 'Where is PC port?',
    rating: 5,
    img: [
      'https://resources.cdn-kaspi.kz/img/m/p/h5d/hff/84374509748254.jpg?format=gallery-medium',
    ],
    link: 'https://kaspi.kz/shop/p/spider-man-2-ps5-113510344/?c=750000000',
    show: true,
  },

  {
    id: 6,
    name: 'Клавиатура X-Game XK-200UB',
    price: 2446,
    description: 'LGBT light',
    rating: 5,
    img: [
      'https://resources.cdn-kaspi.kz/img/m/p/h87/h6b/63813579538462.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/hf9/he4/63813583339550.jpg?format=gallery-medium'
    ],
    link: 'https://kaspi.kz/shop/p/x-game-xk-200ub-chernyi-9200601/?c=750000000',
    show: true,
  },

  {
    id: 7,
    name: 'Клавиатура Ajazz AK820 Pro',
    price: 80000,
    description: 'Keyboard for VIPs',
    rating: 5,
    img: [
      'https://resources.cdn-kaspi.kz/img/m/p/hdf/hfa/84696373461022.png?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/hfe/h6b/84696373526558.png?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h14/hbb/84696373592094.png?format=gallery-medium'
    ],
    link: 'https://kaspi.kz/shop/p/ajazz-ak820-pro-belyi-115277471/?c=750000000',
    show: true,
  },

  {
    id: 8,
    name: 'POCKET BOOK PB970-M-CIS',
    price: 156191,
    description: 'Why need we paper version if we have electronic',
    rating: 5,
    img: [
      'https://resources.cdn-kaspi.kz/img/m/p/hdd/h54/64111136440350.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h3e/h4a/64111139389470.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h51/h0b/64111142338590.jpg?format=gallery-medium'
    ],
    link: 'https://kaspi.kz/shop/p/pocket-book-pb970-m-cis-seryi-103076602/?c=750000000',
    show: true,
  },

  {
    id: 9,
    name: 'Apple iPad 2021',
    price: 154391,
    description: 'Best gadget of Apple?',
    rating: 5,
    img: [
      'https://resources.cdn-kaspi.kz/img/m/p/he4/hdd/64320699203614.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h45/ha8/64320705036318.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/hef/h65/64320710737950.jpg?format=gallery-medium'
    ],
    link: 'https://kaspi.kz/shop/p/apple-ipad-2021-wi-fi-10-2-djuim-3-gb-64-gb-seryi-102301598/?c=750000000',
    show: true,
  },

  {
    id: 10,
    name: 'Samsung Galaxy A54',
    price: 144983,
    description: 'Samsung',
    rating: 5,
    img: [
      'https://resources.cdn-kaspi.kz/img/m/p/hc4/h8b/80435552223262.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h07/h37/80435552747550.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h5d/h8f/80435915292702.jpg?format=gallery-medium'
    ],
    link: 'https://kaspi.kz/shop/p/samsung-galaxy-a54-5g-6-gb-128-gb-chernyi-110044409/?c=750000000',
    show: true,
  },
];

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
