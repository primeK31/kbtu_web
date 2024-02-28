import { Component, Input, Output } from '@angular/core';
import { categories } from '../categories';
import { products } from '../products'; 
import { Product } from '../products'; 

@Component({
  selector: 'app-like',
  templateUrl: './like.component.html',
  styleUrl: './like.component.css'
})
export class LikeComponent {
  products = [...products]
  categories = [...categories]
  @Input() likes: number = 0;
  @Input() p: Product = products[1];
  isLiked = false;
  toggleLike(): void {
    this.isLiked = !this.isLiked;
    if (this.isLiked) {
      this.likes++;
    } else {
      this.likes--;
    }
  }
}
