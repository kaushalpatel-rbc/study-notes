# Hooks

Hooks let us "hook" into React's features without having to write a class. React comes with built-in hooks and can work with custom hooks.

All hooks, by convention, start with `use`. This is what identifies them as a hook in a React project.

There are 5 common categories built-in React hooks fall under:

1. State Hooks: Manage info within a component
2. Context Hooks: Access info from a distant parent
3. Ref Hooks: Manage info within a component that isn't used for rendering
4. Effect Hooks: Connect and synchronize with a external system
5. Performance Hooks: Reduce work between renders to improve performance

## Basic Hooks

The `useState` and `useEffect` hooks are the most commonly used in a React component.

### useState

The `useState` hook is used to manage component state and trigger a re-render when state is updated.

`useState` provides the initial data value and a function to update the state.

```jsx
import { useState } from "react";

const [data, setData] = useState(0);
```

[useState](https://react.dev/reference/react/useState)

### useEffect

The `useEffect` hook is used to connect and synchronize with an external system i.e. data from an external DB.

`useEffect` takes 2 parameters and consists of 3 parts.

1. A side effect function, `() => {}`, as the 1st param
2. A dependency array, `[]`, as the 2nd param
3. Optionally, a return function that runs a cleanup code on re-render or component unmount based on the dependency array

_When the dependecy array is empty, the side effect will run at least once on component mount._

[useEffect](https://react.dev/reference/react/useEffect)

## Common Hooks

### useContext

The `useContext` hook is used to pass data between many components without having to pass props down through the component tree.

`useContext` returns a context object based on the closest context provider in the component tree. A context provider is created by using `createContext` and passing the initial values to be set in the context.

```jsx
import {useContext, createContext} from "react";

const ThemeContext = createContext({})

const App = () => {
  const theme = {}

  return (
    <ThemeContext.Provider value={theme}>
      <Page />
    </ThemeContext.Provider>
  )
}

const Page = (props) => {
  const theme = useContext(ThemeContext)
  ...
}
```

[useContext](https://react.dev/reference/react/useContext)

### useRef

The `useRef` hook provides a way to create a mutable reference that persists between re-renders.

```jsx
import { useRef } from "react";

const App = () => {
  const countRef = useRef(0);
};
```

This `ref` value can also be used to reference a DOM node or another React element.

```jsx
import {useRef} from 'react'

const App = () => {
  const inputRef = useRef(null)

  const handleClick = () => {
    inputRef.current.focus()
  }

  return (
    <input ref={inputRef} />
    <button onClick={handleClick}>Click to focus on input</button>
  )
}
```

[useRef](https://react.dev/reference/react/useRef)

### useMemo

### useReducer

### useCallback

## Custom Hooks

Custom hooks are a way to extract component logic into reusable functions following React principles.

Any function that calls React hooks, by convention, has the prefix `use`. This way, it's easy to identify what functions can cause a re-render of a component.

Custom Hooks let you share stateful logic but not state itself. Each call to a Hook is completely independent from every other call to the same Hook.

Hooks must follow React's principle of being pure, a given input should result in the same output, this is because the hook will re-run on every render. Values from one hook can be passed to another hook, effectively creating a chain of inputs and outputs that are refreshed with every update and render.

[Custom Hook Best Practice](https://react.dev/reference/rules/rules-of-hooks)

There are 2 rules with React Hooks:

1. Only call Hooks from the top-level

- Hooks must be called from the root of a function component or another custom Hook
- Hooks cannot be called from a loop, function, or any other nested scope

2. Only call Hooks from React functions

- Do not call Hooks from JS functions
- This ensures that all stateful logic in a component is clearly visible from its source code
