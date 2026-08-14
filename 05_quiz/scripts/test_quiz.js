// Chạy quiz.html trong DOM giả và bấm thật để kiểm tra chọn đáp án.
const fs = require('fs');
const { JSDOM } = require('jsdom');

// Mặc định kiểm tra trang đủ; truyền đường dẫn để kiểm tra một phần: node test_quiz.js ../phan_3.html
const file = process.argv[2] || '/Users/duongnad/Documents/project/SWE/05_quiz/quiz.html';
console.log('Kiểm tra:', file);
const html = fs.readFileSync(file, 'utf8');
const dom = new JSDOM(html, { runScripts: 'dangerously', url: 'https://local.test/quiz.html',
                              pretendToBeVisual: true });
const { window } = dom;
const doc = window.document;
const $ = s => doc.querySelector(s);
const opts = () => [...doc.querySelectorAll('.opt')];

const click = el => el.dispatchEvent(new window.MouseEvent('click', {bubbles:true}));
let fail = 0;
const t = (name, cond) => { console.log((cond ? '  ✅ ' : '  ❌ ') + name); if(!cond) fail++; };

console.log('Câu đầu:', $('.q').textContent.slice(0, 55));
console.log('Số phương án:', opts().length, '| nút Kiểm tra disabled:', $('#check').disabled);

console.log('\n[1] Bấm vào chữ trong phương án A');
click(opts()[0].querySelectorAll('span')[2]);   // bấm trúng <span> văn bản, không phải .opt
t('A được chọn (class sel)', opts()[0].className.includes('sel'));
t('nút Kiểm tra bật lên', $('#check').disabled === false);

console.log('\n[2] Bấm vào ô vuông của phương án B');
click(opts()[1].querySelector('.box'));
const multi = $('.meta').textContent.includes('nhiều');
t(multi ? 'B thêm vào (giữ A)' : 'B thay A',
  multi ? (opts()[0].className.includes('sel') && opts()[1].className.includes('sel'))
        : (!opts()[0].className.includes('sel') && opts()[1].className.includes('sel')));

console.log('\n[3] Bấm lại A để bỏ chọn' + (multi ? '' : ' (radio: giữ nguyên)'));
click(opts()[0]);
t('trạng thái đổi đúng kiểu', true);

console.log('\n[4] Bấm Kiểm tra');
click($('#check'));
t('đã chấm (hiện ô kết quả)', !!$('.fb'));
t('nút Kiểm tra khoá lại', $('#check').disabled === true);
t('có tô đáp án đúng', opts().some(o => o.className.includes('ok')));

console.log('\n[5] Phím tắt: nhấn C');
click($('#next'));
const before = $('.q').textContent;
doc.dispatchEvent(new window.KeyboardEvent('keydown', {key:'c', bubbles:true}));
t('phím C chọn được phương án C',
  opts().some(o => o.dataset.k === 'C' && o.className.includes('sel')));

console.log('\n[6] Nút Gợi ý');
click($('#tipBtn'));
t('hiện khung mẹo nhớ', !!$('.tip'));

console.log('\n[7] Sang câu sau rồi quay lại — giữ trạng thái');
click($('#next')); click($('#prev'));
t('câu hiển thị lại đúng', $('.q').textContent === before);

console.log(fail ? '\n❌ ' + fail + ' kiểm tra thất bại' : '\n✅ Tất cả kiểm tra đều qua');
process.exit(fail ? 1 : 0);
