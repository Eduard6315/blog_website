import { mount } from 'vitest';
import PostList from '@/components/PostList.vue';

describe('PostList', () => {
  test('renders a list of posts', () => {
    const wrapper = mount(PostList);
    // здесь можно писать проверки на ожидаемое поведение компонента
  });
});