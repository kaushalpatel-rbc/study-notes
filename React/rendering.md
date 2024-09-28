# Rendering

React follows a declarative approach to rendering components. This means developers can specify what the component should look like, and React takes care of rendering the component.

A virtual DOM (VDOM), a lightweight, in-memory representation of the DOM, is used by React to optimize rendering of components.

The general [render and commit](https://react.dev/learn/render-and-commit) process looks like this:

1. (Trigger) A component is written in JSX with a defined render method that returns what a component should look like
2. (Render) When a component is rendered, React will create a VDOM representation of it
3. (Render) React compares the current and previous VDOM representations of a component, and when a difference is found it calculates the minimum number of DOM manipulations to bring the DOM up-to-date with the latest VDOM
4. (Commit) React updates the DOM with the calculated differences

Below are the core concepts that play a part when React renders or has to re-render a component.

## Component Lifecycle

There are 3 common stages to a React components lifecycle; Mounting, Updating, and Unmounting.

**Mounting**: A component _mounts_ when it's added to the screen
**Updating**: A component _updates_ when it receives new props or state, usually in response to an interaction i.e. event, or new data
**Unmounting**: A component _unmounts_ when it's removed from the screen

## Lists and Keys

React is able to render a collection of items using simple JS functions like `map()` and `filter()`. The caveat being, each rendered item must contain a `key` prop to uniquely identify it during a re-render.

[Why does React need keys?](https://react.dev/learn/rendering-lists#why-does-react-need-keys)

## Render Props

A commonly used pattern to render components by passing a `render` prop defining how they should be rendered within a parent component.

```
const Title = (props) => props.render()

<Title render={() => <h1>This is a render prop</h1>}>
```

This patterns helps reduce the risk of lifting state to share it between siblings by encapsulating components and passing the data through a render prop.

With the introdution of hooks, this patterns is seldomly used.

[Render Props Pattern](https://www.patterns.dev/react/render-props-pattern/)

## Refs

Refs give the developer a way to access DOM nodes and React elements without triggering a re-render. A `ref` is a means of storing non-state data on a component instance.

A `ref` is intentionally mutable, meaning the actual value can be updated. Every `ref` object is a simple JS object with a `current` property that holds any type of data passed to it.

[Differences between refs and state](https://react.dev/learn/referencing-values-with-refs#differences-between-refs-and-state)

Refs are meant to be an 'escape hatch' from React's way of managing data and component rendering. It should be used sparingly and with the right intention in mind to avoid rendering bugs.

**forwardRef** is a special React function to access another components DOM node, by default React will complain if a `ref` prop is applied to a component that does not allow its ref to be accessed.

## Events

React components can handle browser events by using custom event handler functions. Event listeners can be added to a component as a prop with a reference to a handler function.

Each handler function has access to a `synthetic event` object, similar to a DOM event object but fixed for some browser inconsistencies.
[React event object](https://react.dev/reference/react-dom/components/common#react-event-object)
