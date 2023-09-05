function solve() {

let title = document.getElementById(`task-title`);
let category = document.getElementById(`task-category`);
let content = document.getElementById(`task-content`);
let publishBtn = document.getElementById(`publish-btn`);
let reviewUl = document.getElementById(`review-list`);
let publishedUl = document.getElementById(`published-list`);

publishBtn.addEventListener(`click`, publishEvent);

function publishEvent(event){
    event.preventDefault();

    if (title.value == `` || category.value == `` || content.value == ``){
        return;
    }

    let parentLi = createElement(`li`, reviewUl, null, [`rpost`])
    let parentArt = createElement(`article`, parentLi);
    createElement(`h4`, parentArt, `${title.value}`);
    createElement(`p`, parentArt, `Category: ${category.value}`);
    createElement(`p`, parentArt, `Content: ${content.value}`);
    let editBtn = createElement(`button`, parentLi, `Edit`, [`action-btn`]);
    editBtn.classList.add(`edit`);
    let postBtn = createElement(`button`, parentLi, `Post`, [`action-btn`]);
    postBtn.classList.add(`post`);

    editBtn.addEventListener(`click`, editPostsEvent);
    postBtn.addEventListener(`click`, postEvent);


    title.value = ``;
    category.value = ``;
    content.value = ``; 
}

function editPostsEvent(event){
    event.preventDefault();
    let parent = this.parentNode;
    let currTitle =  parent.querySelector(`h4`).textContent;
    console.log(parent)
    let currCat = parent.querySelectorAll(`p`)[0].textContent;
    let currCont = parent.querySelectorAll(`p`)[1].textContent;
    let trimTitle = currTitle.replace("Title: ", "");
    let trimCat = currCat.replace("Category: ", "");
    let trimCont = currCont.replace("Content: ", "");
    title.value = trimTitle;
    category.value = trimCat;
    content.value = trimCont;
    parent.remove();
   

}

function postEvent(event){
    event.preventDefault();
    let parent = this.parentNode;
    let edBtn = parent.querySelector('button.action-btn.edit');
    let poBtn = parent.querySelector(`button.action-btn.post`);
    edBtn.remove();
    poBtn.remove();
    publishedUl.appendChild(parent);
    


}

function createElement(
    type,
    parentNode,
    content,
    classes,
    id,
    attributes,
    useInnerHtml
  ) {
    const htmlElement = document.createElement(type);

    if (content && useInnerHtml) {
      htmlElement.innerHTML = content;
    } else {
      if (content && type !== "input") {
        htmlElement.textContent = content;
      }

      if (content && type === "input") {
        htmlElement.value = content;
      }
    }

    if (classes && classes.length > 0) {
      htmlElement.classList.add(...classes);
    }

    if (id) {
      htmlElement.id = id;
    }

    // { src: 'link', href: 'http' }
    if (attributes) {
      for (const key in attributes) {
        htmlElement.setAttribute(key, attributes[key]);
      }
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    return htmlElement;
  }


 
}
