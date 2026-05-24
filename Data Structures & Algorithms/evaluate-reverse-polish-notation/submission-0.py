class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operators:
                # This safely handles negative strings like "-11"
                st.append(int(token))
            else:
                # The first pop is the second operand (f), the second is the first (s)
                f = st.pop()
                s = st.pop()
                
                if token == '+':
                    st.append(s + f)
                elif token == '-':
                    st.append(s - f)
                elif token == '*':
                    st.append(s * f)
                elif token == '/':
                    # int() truncates toward zero, which is required for this problem
                    st.append(int(s / f))

        return st[0]