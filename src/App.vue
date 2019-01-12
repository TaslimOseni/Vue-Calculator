<template>
  <div class="calculator">
    <div class="display">{{current || '0'}}</div>
    
    <div @click="clear" class="btn clear operator">CLEAR</div>

    <div @click="add" class="btn operator">+</div>
    <div @click="minus" class="btn operator">-</div>
    <div @click="divide" class="btn operator">÷</div>
    <div @click="times" class="btn operator">x</div>

    
    <div @click="append('7')" class="btn">7</div>
    <div @click="append('8')" class="btn">8</div>
    <div @click="append('9')" class="btn">9</div>

    <div @click="append('4')" class="btn">4</div>
    <div @click="append('5')" class="btn">5</div>
    <div @click="append('6')" class="btn">6</div>
    
    <div @click="append('1')" class="btn">1</div>
    <div @click="append('2')" class="btn">2</div>
    <div @click="append('3')" class="btn">3</div>

    <div @click="dot" class="btn">.</div>
    <div @click="append('0')" class="btn">0</div>
    <div @click="equal" class="btn equal">=</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      previous: null,
      current: '',
      operator: null,
      operatorClicked: false,
    }
  },
  methods: {
    clear() {
      this.current = '';
    },
    append(number) {
      if (this.operatorClicked) {
        this.current = '';
        this.operatorClicked = false;
      }
      this.current = `${this.current}${number}`;
    },
    dot() {
      if (this.current.indexOf('.') === -1) {
        this.append('.');
      }
    },
    setPrevious() {
      this.previous = this.current;
      this.operatorClicked = true;
    },
    divide() {
      this.operator = (a, b) => a / b;
      this.setPrevious();
    },
    times() {
      this.operator = (a, b) => a * b;
      this.setPrevious();
    },
    minus() {
      this.operator = (a, b) => a - b;
      this.setPrevious();
    },
    add() {
      this.operator = (a, b) => a + b;
      this.setPrevious();
    },
    equal() {
      this.current = `${this.operator(
        parseFloat(this.current), 
        parseFloat(this.previous)
      )}`;
      this.previous = null;
    }
  }
}


</script>

<style scoped>
.calculator{
  margin: 0 auto;
  margin-top: 200px;
  width: 300px;
  font-size: 30px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: minmax(50px, auto);
}

.display{
  grid-column: 1 / 4;
  background-color: #BBB;
  text-align: center;
  color: #000;
}

.btn{
  background-color: #F2F2F2;
  border: 1px solid #999;
  text-align: center;
}

.operator{
  background-color: #ffff90;
  color: #555;
}

.clear{
  grid-column: 1/3;
  color: red;
  font-size: 30px;
  text-align: center;
}

.equal{
  background-color: green;
  color: white;
}


</style>